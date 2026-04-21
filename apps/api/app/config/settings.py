from pathlib import Path
from typing import ClassVar

import httpx
from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 6379
    USERNAME: str | None = None
    PASSWORD: str | None = None


class Settings(BaseSettings):
    redis: RedisSettings = RedisSettings()
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "uz-plan-api"
    SCHEDULE_LINK: str = "https://plan.uz.zgora.pl/grupy_plan.php?ID="
    SUPPORTED_MAJOR: httpx.URL = httpx.URL(
        "https://plan.uz.zgora.pl/grupy_lista_grup_kierunku.php?ID=401"
    )
    GROUPS_FILE: ClassVar[Path] = (
        Path(__file__).resolve().parents[2] / "groups.json"
    )
    LONGEST_ID: int = 5

    model_config = {"env_nested_delimiter": "__"}


settings = Settings()
