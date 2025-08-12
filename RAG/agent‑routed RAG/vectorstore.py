from typing import List

from .config import require_env
from .data_loading import load_and_split_documents


def initialize_astra() -> None:
    """Initialize Cassio (DataStax Astra DB) connection from environment."""
    import cassio

    astra_token = require_env("ASTRA_DB_APPLICATION_TOKEN")
    astra_db_id = require_env("ASTRA_DB_ID")
    cassio.init(token=astra_token, database_id=astra_db_id)


def _import_cassandra_vectorstore():
    """Support both new and legacy import paths for the Cassandra vectorstore."""
    try:
        from langchain_community.vectorstores.cassandra import Cassandra  # type: ignore
        return Cassandra
    except Exception:
        from langchain.vectorstores.cassandra import Cassandra  # type: ignore
        return Cassandra


def build_cassandra_vectorstore(table_name: str = "medical_cds_docs"):
    """Create a Cassandra vector store backed by Astra DB using HuggingFace embeddings."""
    from langchain_huggingface import HuggingFaceEmbeddings

    Cassandra = _import_cassandra_vectorstore()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_store = Cassandra(
        embedding=embeddings,
        table_name=table_name,
        session=None,
        keyspace=None,
    )
    return vector_store


def ensure_index(vector_store, urls: List[str]) -> None:
    """Index provided URLs into the vector store if table is empty; otherwise, skip."""
    try:
        _ = vector_store.similarity_search("test", k=1)
        if _:
            return
    except Exception:
        pass

    docs = load_and_split_documents(urls)
    vector_store.add_documents(docs)
    table_name = getattr(vector_store, "table_name", "cassandra_table")
    print(f"Inserted {len(docs)} chunks into '{table_name}'.")


