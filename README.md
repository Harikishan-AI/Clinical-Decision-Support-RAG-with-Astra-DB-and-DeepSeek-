# **AI Agent RAG — Clinical Decision Support**  
*(Astra DB + LangChain + LangGraph + Groq + LangSmith + SerpAPI)*

An **agent‑routed Retrieval‑Augmented Generation (RAG)** system for **Clinical Decision Support (CDS)**, combining:

- **Astra DB Vector Database** — indexes and retrieves clinical guidelines, medication safety data, dosing protocols, contraindications, diagnostic criteria, and care pathways for evidence‑grounded answers.  
- **SerpAPI Web Search** — fallback search tool (via LangChain) for broader or out‑of‑domain medical background.  
- **LangGraph** — orchestrates routing and workflow between retrieval and fallback tools.  
- **DeepSeek LLM (via Groq API)** — performs intelligent query routing and reasoning.  
- **LangSmith** — provides real‑time tracing, monitoring, and evaluation (precision, latency, debugging) for continuous pipeline optimization.

---

## **Features**
- **Agent‑Routed RAG**: LLM dynamically decides between vectorstore or SerpAPI search based on the query intent.  
- **LangGraph State Machine**: Modular nodes for retrieval, fallback, and response generation.  
- **Astra DB Vectorstore** with HuggingFace embeddings for fast and scalable semantic search.  
- **SerpAPI Integration** (via LangChain) for up‑to‑date web search results.  
- **LangSmith Monitoring**: End‑to‑end observability for debugging, performance tracking, and evaluation.  
- **Environment‑Based Config**: `.env` file support for credentials and settings.  
- **Easily Extensible**: Integrate PubMed, PMC, or specialty APIs by adding new tools and routing logic.

---

## **Prerequisites**
- **Python** 3.10+ (recommended)
- **DataStax Astra DB** credentials:
  - `ASTRA_DB_APPLICATION_TOKEN`
  - `ASTRA_DB_ID`
- **Groq API Key** — for DeepSeek LLM
- **SerpAPI API Key** — for web search fallback
- (Optional, Recommended) **LangSmith API Key** — for monitoring
