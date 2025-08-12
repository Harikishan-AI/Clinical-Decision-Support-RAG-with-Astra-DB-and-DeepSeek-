import os

from .config import require_env


def create_router():
    """Create an LLM router (Groq) that chooses between vectorstore and web search (SerpAPI)."""
    from typing import Literal
    from langchain_core.pydantic_v1 import BaseModel, Field
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_groq import ChatGroq

    groq_api_key = require_env("GROQ_API_KEY")
    model_name = (os.environ.get("GROQ_MODEL") or "deepseek-r1-distill-llama-70b").strip()

    class RouteQuery(BaseModel):
        """Route a user query to the most relevant datasource."""

        datasource: Literal["vectorstore", "web_search"] = Field(
            ...,
            description=(
                "Choose 'vectorstore' for clinical guidelines, diagnosis, meds, procedures, or 'web_search' otherwise."
            ),
        )

    llm = ChatGroq(groq_api_key=groq_api_key, model_name=model_name)
    structured_llm_router = llm.with_structured_output(RouteQuery)

    system = (
        "You route user questions to either a vectorstore or general web search via SerpAPI.\n"
        "The vectorstore contains medical clinical decision support content: clinical guidelines, medication safety info, "
        "diagnostic criteria, and care pathways.\n"
        "Use the vectorstore for questions about diagnoses, treatments, medications, dosing, contraindications, "
        "clinical guidelines, and care pathways. Otherwise, use web_search."
    )
    route_prompt = ChatPromptTemplate.from_messages(
        [("system", system), ("human", "{question}")]
    )

    question_router = route_prompt | structured_llm_router
    return question_router


