import os
from dataclasses import dataclass


@dataclass(frozen=True)
class WebTargetContract:
    dashboard_path: str
    project_cards_container_selector: str
    heading_keywords: tuple[str, ...]
    title_keywords: tuple[str, ...]
    lede_keywords: tuple[str, ...]


def _csv_env(key: str, fallback: tuple[str, ...]) -> tuple[str, ...]:
    raw = os.getenv(key)
    if not raw:
        return fallback
    values = tuple(part.strip() for part in raw.split(",") if part.strip())
    return values or fallback


def _profile_qa_portfolio_live_site() -> WebTargetContract:
    return WebTargetContract(
        dashboard_path=os.getenv("WEB_DASHBOARD_PATH", "dashboard.html"),
        project_cards_container_selector=os.getenv("WEB_PROJECT_CARDS_SELECTOR", "#project-cards"),
        heading_keywords=_csv_env("WEB_HEADING_KEYWORDS", ("automation", "results", "evidence")),
        title_keywords=_csv_env("WEB_TITLE_KEYWORDS", ("automation", "results", "evidence")),
        lede_keywords=_csv_env("WEB_LEDE_KEYWORDS", ("ci", "status", "workflow")),
    )


_WEB_TARGET_PROFILES = {
    "qa_portfolio_live_site": _profile_qa_portfolio_live_site,
}


def load_web_contract(profile_name: str) -> WebTargetContract:
    builder = _WEB_TARGET_PROFILES.get(profile_name)
    if builder is None:
        supported = ", ".join(sorted(_WEB_TARGET_PROFILES.keys()))
        raise ValueError(f"Unsupported WEB_TARGET_PROFILE '{profile_name}'. Supported profiles: {supported}")
    return builder()
