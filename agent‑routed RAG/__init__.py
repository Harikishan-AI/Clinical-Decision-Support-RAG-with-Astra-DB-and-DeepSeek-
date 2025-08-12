"""Agentic RAG package.

Modular implementation of a routed RAG system using Astra DB (CassIO) as a
vector store and SerpAPI-backed web search as a fallback datasource, with
routing handled by a Groq-served LLM. LangSmith tracing can be enabled via env.
"""

__all__ = [
    "config",
    "data_loading",
    "graph",
    "router",
    "tools",
    "vectorstore",
]


