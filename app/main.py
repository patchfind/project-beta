from __future__ import annotations

import argparse

from app.config import Settings
from app.data import load_documents
from app.graph import create_rag_graph
from app.guardrails import validate_prompt
from app.observability import configure_phoenix
from app.vector_store import build_vector_store, load_vector_store


def build_sample_app():
    settings = Settings()
    documents = load_documents()

    if settings.vector_store_path.exists():
        vector_store = load_vector_store(settings.vector_store_path)
    else:
        vector_store = build_vector_store(documents, settings.vector_store_path)

    return create_rag_graph(vector_store)


def main() -> None:
    configure_phoenix()
    parser = argparse.ArgumentParser(description="Run the sample LangGraph RAG app.")
    parser.add_argument("--query", default="What does this sample project do?", help="Question to answer.")
    args = parser.parse_args()

    validate_prompt(args.query)
    graph = build_sample_app()
    response = graph.invoke({"question": args.query})
    print(response["answer"])


if __name__ == "__main__":
    main()
