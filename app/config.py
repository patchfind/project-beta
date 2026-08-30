from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Settings:
    project_name: str = "project-beta-sample-rag"
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    llm_model: str = os.getenv("LLM_MODEL", "distilgpt2")
    docs_path: Path = Path(os.getenv("DOCS_PATH", str(BASE_DIR / "data" / "sample_docs.txt")))
    vector_store_path: Path = Path(os.getenv("VECTOR_STORE_PATH", str(BASE_DIR / "storage" / "faiss_index")))
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    phoenix_endpoint: str = os.getenv("PHOENIX_ENDPOINT", "http://localhost:6006")
    guardrails_config: Path = Path(os.getenv("GUARDRAILS_CONFIG", str(BASE_DIR / "config" / "guardrails_config.yml")))
