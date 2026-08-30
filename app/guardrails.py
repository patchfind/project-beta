from __future__ import annotations

from pathlib import Path

from app.config import Settings

BLOCKED_PATTERNS = ("bypass", "hack", "exploit", "ignore rules")


def validate_prompt(question: str) -> str:
    lowered = question.lower()
    if any(pattern in lowered for pattern in BLOCKED_PATTERNS):
        raise ValueError("The prompt was rejected by the sample guardrail policy.")
    return question


def guardrail_config_path() -> Path:
    return Settings().guardrails_config
