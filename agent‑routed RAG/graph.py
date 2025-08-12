from typing import Any, Dict, List, Union


def build_graph(question_router, retriever, web_search_tool):
    """Build a LangGraph state graph that routes to RAG (AstraDB retriever) or SerpAPI web search."""
    from typing_extensions import TypedDict

    try:
        from langchain_core.documents import Document
    except Exception:  # Fallback for older LangChain
        from langchain.schema import Document  # type: ignore

    from langgraph.graph import END, START, StateGraph

    class GraphState(TypedDict):
        question: str
        generation: str
        documents: Union[List[Document], Document]

    def retrieve(state: Dict[str, Any]) -> Dict[str, Any]:
        print("---RETRIEVE (Vectorstore/RAG)---")
        question = state["question"]
        documents = retriever.invoke(question)
        return {"documents": documents, "question": question}

    def web_search(state: Dict[str, Any]) -> Dict[str, Any]:
        print("---WEB SEARCH (SerpAPI)---")
        question = state["question"]
        result_text = web_search_tool.invoke({"query": question})
        wiki_doc = Document(page_content=result_text)
        return {"documents": wiki_doc, "question": question}

    def route_question(state: Dict[str, Any]) -> str:
        print("---ROUTE QUESTION---")
        question = state["question"]
        source = question_router.invoke({"question": question})
        chosen = (
            source.get("datasource") if isinstance(source, dict) else getattr(source, "datasource", None)
        )
        if chosen == "web_search":
            print("---ROUTE → Web Search---")
            return "web_search"
        print("---ROUTE → Vectorstore (RAG)---")
        return "vectorstore"

    workflow = StateGraph(GraphState)
    workflow.add_node("web_search", web_search)
    workflow.add_node("vectorstore", retrieve)

    workflow.add_conditional_edges(
        START,
        route_question,
        {"web_search": "web_search", "vectorstore": "vectorstore"},
    )
    workflow.add_edge("vectorstore", END)
    workflow.add_edge("web_search", END)
    app = workflow.compile()
    return app


