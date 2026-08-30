# Project Beta: Minimal LangGraph RAG Sample

This repository is a small, modular sample app that combines:

- LangChain and LangGraph for orchestration
- PyTorch and Transformers for local model inference
- FAISS for vector search
- Redis and Phoenix placeholders for production-friendly storage and tracing
- vLLM for optional high-throughput inference
- Ragas for evaluation hooks
- NeMo Guardrails for safety controls

The sample intentionally uses the simplest practical models:

- Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
- Generation: `distilgpt2`

This keeps the project approachable and easy to run on a laptop while still illustrating the architecture.

## Project layout

- `app/config.py` — environment-driven settings
- `app/data.py` — document loading helpers
- `app/vector_store.py` — FAISS vector store build and load utilities
- `app/graph.py` — LangGraph workflow for retrieval + answer generation
- `app/guardrails.py` — simple safety checks and guardrail config path
- `app/observability.py` — optional Phoenix setup
- `app/main.py` — CLI entry point
- `config/guardrails_config.yml` — sample NeMo Guardrails config
- `data/sample_docs.txt` — minimal sample corpus

## Quick start

```bash
python -m venv .venv
# On Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m app.main --query "What does this sample project do?"
```

## Optional services

- Redis: set `REDIS_URL` for a local or remote Redis instance.
- Phoenix: start Phoenix locally, then point `PHOENIX_ENDPOINT` at it.
- vLLM: swap in a faster local inference backend for a production-like serving setup.

## Notes

This project is intentionally compact and not a production-ready deployment. It is meant to be a clear starting point for experimentation with LangGraph, local model inference, and retrieval-augmented generation.
