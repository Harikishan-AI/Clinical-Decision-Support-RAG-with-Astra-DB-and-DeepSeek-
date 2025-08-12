from .config import require_env


def create_web_search_tool():
    """Create SerpAPI web search tool for general background queries.

    Requires environment variable `SERPAPI_API_KEY`.
    Returns a Runnable-like object with `.invoke(...)`.
    """
    from langchain_community.utilities import SerpAPIWrapper
    from langchain_core.runnables import RunnableLambda

    # Ensure key exists early with a helpful error message
    require_env("SERPAPI_API_KEY")

    serp = SerpAPIWrapper()

    def _search(inputs):
        query = inputs.get("query") if isinstance(inputs, dict) else str(inputs)
        return serp.run(query)

    return RunnableLambda(_search)


