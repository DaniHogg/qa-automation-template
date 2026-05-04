import os
from dataclasses import dataclass

from core.api_contract import ApiTargetContract, load_api_contract
from core.web_contract import WebTargetContract, load_web_contract


def _as_bool(value: str, default: bool = True) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://danihogg.github.io/qa-portfolio-livesite/")
    api_base_url: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    browser: str = os.getenv("BROWSER", "chrome")
    headless: bool = _as_bool(os.getenv("HEADLESS", "true"), default=True)
    web_target_profile: str = os.getenv("WEB_TARGET_PROFILE", "qa_portfolio_live_site")
    api_target_profile: str = os.getenv("API_TARGET_PROFILE", "jsonplaceholder")
    login_username: str = os.getenv("LOGIN_USERNAME", "tomsmith")
    login_password: str = os.getenv("LOGIN_PASSWORD", "SuperSecretPassword!")

    @property
    def web_contract(self) -> WebTargetContract:
        return load_web_contract(self.web_target_profile)

    @property
    def api_contract(self) -> ApiTargetContract:
        return load_api_contract(self.api_target_profile)


settings = Settings()
