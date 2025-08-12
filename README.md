# **AI Agent RAG — Clinical Decision Support**  
*(Astra DB + LangChain + LangGraph + Groq + LangSmith + SerpAPI)*

An **agent‑routed Retrieval‑Augmented Generation (RAG)** system for **Clinical Decision Support (CDS)**, combining:

- **Astra DB Vector Database** — indexes and retrieves clinical guidelines, medication safety data, dosing protocols, diagnostic criteria, and care pathways for evidence‑grounded answers.  
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


---

## **How It Works**
1. **Query Routing** — The Groq‑hosted DeepSeek LLM determines whether the user’s query should be answered from the **Astra DB vectorstore** or **SerpAPI search**.  
2. **Semantic Retrieval** — Astra DB stores embeddings of medical guidelines and retrieves the most relevant chunks.  
3. **Fallback Search** — If the LLM detects the query is out‑of‑scope for the vectorstore, SerpAPI provides fresh web search results.  
4. **LangGraph Orchestration** — A state machine manages transitions between routing, retrieval, and responding.  
5. **Monitoring & Evaluation** — LangSmith captures traces, evaluates retrieval precision, and logs latency/performance metrics.

---

## **Extending the Pipeline**
- **Add PubMed/PMC**: Plug in API tools for peer‑reviewed medical literature.  
- **Add Confidence Scoring**: Use verifier nodes to re‑query if results are low quality.  
- **Multi‑Tool Planning**: Upgrade routing to agentic loops for more complex reasoning.

---

## **License**
This project is released under the [MIT License](LICENSE).

