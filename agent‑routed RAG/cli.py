import argparse
from typing import Any, Dict

from .config import load_env
from .vectorstore import (
    initialize_astra,
    build_cassandra_vectorstore,
    ensure_index,
)
from .tools import create_web_search_tool
from .router import create_router
from .graph import build_graph


def run_query(app, question: str) -> None:
    from pprint import pprint

    last_state: Dict[str, Any] | None = None
    for output in app.stream({"question": question}):
        for node_name, node_state in output.items():
            pprint(f"Node '{node_name}':")
            last_state = node_state
        pprint("\n---\n")

    if last_state and "documents" in last_state:
        try:
            docs = last_state["documents"]
            if isinstance(docs, list) and len(docs) > 0:
                meta = getattr(docs[0], "metadata", {}) or {}
                description = meta.get("description")
                if description:
                    print(description)
                else:
                    print(getattr(docs[0], "page_content", ""))
            else:
                print(getattr(docs, "page_content", str(docs)))
        except Exception:
            pass


def main() -> None:
    load_env()

    # Enable LangSmith tracing if env vars are present
    try:
        import os
        # Prefer modern LANGCHAIN_* vars
        if os.environ.get("LANGCHAIN_API_KEY") and os.environ.get("LANGCHAIN_PROJECT"):
            os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
            os.environ.setdefault("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
        # Back-compat: map LANGSMITH_* to LANGCHAIN_*
        elif os.environ.get("LANGSMITH_API_KEY") and os.environ.get("LANGSMITH_PROJECT"):
            os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
            os.environ.setdefault("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
            os.environ.setdefault("LANGCHAIN_API_KEY", os.environ["LANGSMITH_API_KEY"])  # type: ignore[index]
            os.environ.setdefault("LANGCHAIN_PROJECT", os.environ["LANGSMITH_PROJECT"])  # type: ignore[index]
    except Exception:
        pass

    parser = argparse.ArgumentParser(
        description=(
            "Medical CDS RAG with LangChain+LangGraph routing between Astra vectorstore and SerpAPI web search, using DeepSeek via Groq."
        )
    )
    parser.add_argument(
        "--question",
        type=str,
        default="First-line therapy for community-acquired pneumonia in adults?",
        help="Clinical question to run through the routed pipeline",
    )
    parser.add_argument(
        "--table",
        type=str,
        default="medical_cds_docs",
        help="Cassandra table name for the vector store",
    )
    args = parser.parse_args()

    # Initialize Astra DB (vector database)
    initialize_astra()

    # Build vector store (Astra DB) as the vector store
    vector_store = build_cassandra_vectorstore(table_name=args.table)

    # Replace with your preferred open medical CDS resources (examples below):
    urls = [
        # Clinical guidelines and authoritative sources (examples; update as needed)
        "https://www.nice.org.uk/guidance/ng138",  # Example guideline page
        "https://www.who.int/publications",  # WHO publications hub
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC4635749/",  # Example PMC article
    ]
    ensure_index(vector_store, urls)

    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    web_search_tool = create_web_search_tool()
    question_router = create_router()
    app = build_graph(question_router, retriever, web_search_tool)

    run_query(app, args.question)


if __name__ == "__main__":
    main()


