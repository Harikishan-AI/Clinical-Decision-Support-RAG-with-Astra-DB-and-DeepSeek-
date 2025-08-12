## AI Agent RAG (Astra DB + LangChain + LangGraph + Groq)

Built an agent‑routed Clinical RAG system combining Astra DB as the vector database with DeepSeek (via ChatGroq) and LangGraph orchestration for intelligent query routing. The pipeline indexes clinical guidelines, medication safety data, dosing protocols, contraindications, diagnostic criteria, and care pathways into Astra DB embeddings for fast semantic retrieval, while an LLM directs out‑of‑domain queries to a Wikipedia fallback. Modular LangGraph nodes (retrieve, fallback, respond) enable low‑latency, scalable retrieval and easy extension (e.g., PubMed/PMC tools). Designed with agentic RAG principles—LLM‑based tool choice and query analysis—with a clear upgrade path to iterative verification and multi‑tool planning. Environment‑based .env configuration ensures portability and Astra DB’s vector‑native capabilities improve recall and relevance for clinical decision support.

- **Vectorstore (Astra DB)** for clinical guidelines, meds, dosing, contraindications, diagnostic criteria, and care pathways
- **Wikipedia** as a fallback for general medical background

Routing is performed by a Groq-served LLM.

### Features
- **LangGraph** state machine for routing and retrieval
- **Astra DB (Cassandra)** vector store with HuggingFace embeddings
- **Wikipedia** fallback tool
- **Environment-based configuration** via `.env`

### Prerequisites
- Python 3.10+ recommended
- DataStax Astra DB credentials (Application Token and Database ID)
- Groq API key

### Quickstart (Windows PowerShell)

1) Clone this repository or open the project folder.

2) Create and use a virtual environment, then install dependencies:

```powershell
python -m venv .venv
./.venv/Scripts/python.exe -m pip install --upgrade pip
./.venv/Scripts/python.exe -m pip install -r requirements.txt
```

### Configuration
Copy `.env.example` to `.env` and set:

```
ASTRA_DB_APPLICATION_TOKEN=...
ASTRA_DB_ID=...
GROQ_API_KEY=...
# Optional override (defaults to deepseek-r1-distill-llama-70b)
# GROQ_MODEL=deepseek-r1-distill-llama-70b
```







