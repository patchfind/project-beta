from __future__ import annotations

from pathlib import Path

from app.config import Settings


def load_documents(path: Path | str | None = None) -> list[str]:
    settings = Settings()
    docs_path = Path(path) if path else settings.docs_path
    text = docs_path.read_text(encoding="utf-8")
    return [segment.strip() for segment in text.split("\n\n") if segment.strip()]
