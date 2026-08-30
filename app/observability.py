from __future__ import annotations

import os

from app.config import Settings


def configure_phoenix() -> None:
    settings = Settings()
    os.environ.setdefault("PHOENIX_COLLECTOR_ENDPOINT", settings.phoenix_endpoint)

    try:
        from phoenix.otel import register

        register()
    except Exception:
        # The project is intentionally lightweight; Phoenix can be enabled in a real deployment.
        pass
