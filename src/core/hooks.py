"""
pytest hooks for failure diagnostics.

Provides:
  - screenshot_on_failure  – captures a browser screenshot on web test failures
  - api_logging_session    – logs every HTTP request and response to the console
"""
from __future__ import annotations

import logging
from pathlib import Path

import pytest
import requests

logger = logging.getLogger(__name__)

# ── Screenshot on failure ────────────────────────────────────────────────────

SCREENSHOT_DIR = Path("screenshots")


def _take_screenshot(driver, node_id: str) -> Path | None:
    """Save a PNG screenshot and return its path, or None on error."""
    try:
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        safe_name = node_id.replace("/", "_").replace("::", "__").replace(" ", "_")
        path = SCREENSHOT_DIR / f"{safe_name}.png"
        driver.save_screenshot(str(path))
        return path
    except Exception as exc:  # noqa: BLE001
        logger.warning("Screenshot capture failed: %s", exc)
        return None


# ── Request / response logging ───────────────────────────────────────────────

class _LoggingAdapter(requests.adapters.HTTPAdapter):
    """Logs request and response details at DEBUG level."""

    def send(self, request: requests.PreparedRequest, **kwargs):
        logger.debug(
            ">> %s %s | headers: %s | body: %s",
            request.method,
            request.url,
            dict(request.headers),
            request.body,
        )
        response = super().send(request, **kwargs)
        logger.debug(
            "<< %s %s | elapsed: %.3fs | body: %.500s",
            response.status_code,
            response.url,
            response.elapsed.total_seconds(),
            response.text,
        )
        return response


def attach_logging_adapter(session: requests.Session) -> None:
    """Mount the logging adapter on both http:// and https:// prefixes."""
    adapter = _LoggingAdapter()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
