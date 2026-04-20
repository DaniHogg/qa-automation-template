import os
from dataclasses import dataclass


def _as_bool(value: str, default: bool = True) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
    api_base_url: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    browser: str = os.getenv("BROWSER", "chrome")
    headless: bool = _as_bool(os.getenv("HEADLESS", "true"), default=True)


settings = Settings()
