from __future__ import annotations

from pathlib import Path

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from app.config import Settings


def build_vector_store(documents: list[str], persist_path: Path | str | None = None) -> FAISS:
    settings = Settings()
    target = Path(persist_path) if persist_path else settings.vector_store_path
    target.parent.mkdir(parents=True, exist_ok=True)

    embeddings = HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={"device": "cpu"},
    )
    vector_store = FAISS.from_texts(documents, embeddings)
    vector_store.save_local(str(target))
    return vector_store


def load_vector_store(persist_path: Path | str | None = None) -> FAISS:
    settings = Settings()
    target = Path(persist_path) if persist_path else settings.vector_store_path
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={"device": "cpu"},
    )
    return FAISS.load_local(str(target), embeddings, allow_dangerous_deserialization=True)
