from typing import List


def load_and_split_documents(urls: List[str]):
    """Load web pages and split into chunks using a token-aware splitter."""
    from langchain_community.document_loaders import WebBaseLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    loaded_docs = []
    for url in urls:
        loaded_docs.extend(WebBaseLoader(url).load())

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=600, chunk_overlap=60
    )
    return splitter.split_documents(loaded_docs)


