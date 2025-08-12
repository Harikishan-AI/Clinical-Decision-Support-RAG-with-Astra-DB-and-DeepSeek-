def create_wikipedia_tool():
    """Create Wikipedia tool as a fallback for general background."""
    from langchain_community.utilities import WikipediaAPIWrapper
    from langchain_community.tools import WikipediaQueryRun

    wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=400)
    wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
    return wiki_tool


