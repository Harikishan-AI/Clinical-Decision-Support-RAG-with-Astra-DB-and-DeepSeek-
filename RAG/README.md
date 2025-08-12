## AI Agent RAG (Astra DB + LangChain + LangGraph + Groq)

An end-to-end, modular RAG system that routes clinical questions between:

- **Vectorstore (Astra DB)** for clinical guidelines, meds, dosing, contraindications, diagnostic criteria, and care pathways
- **Wikipedia** as a fallback for general medical background

Routing is performed by a Groq-served LLM.

### Features
- **LangGraph** state machine for routing and retrieval
- **Astra DB (Cassandra)** vector store with HuggingFace embeddings
- **Wikipedia** fallback tool
- **Environment-based configuration** via `.env`

### Project Structure
```
agentic_rag/
  __init__.py
  __main__.py
  cli.py
  config.py
  data_loading.py
  graph.py
  router.py
  tools.py
  vectorstore.py
requirements.txt
.env.example
.gitignore
README.md
```

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

3) Configure environment variables:

```powershell
Copy-Item .env.example .env
# Edit .env to set: ASTRA_DB_APPLICATION_TOKEN, ASTRA_DB_ID, GROQ_API_KEY
```

4) Run the app:

```powershell
./.venv/Scripts/python.exe -m agentic_rag --question "First-line therapy for community-acquired pneumonia in adults?" --table "medical_cds_docs"
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

### Notes
- The first run will attempt to index example sources into the Cassandra table if it's empty. You can update URLs inside `agentic_rag/cli.py`.
- If you encounter import differences across LangChain versions, the code includes small compatibility shims.

### License
MIT


