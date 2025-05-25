"""App settings."""

from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings."""

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "HeartMeter"
    VERSION: str = "0.1.0"

    class Config:
        """Pydantic config."""

        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """Get app settings.

    Returns:
        Settings: (Settings) App settings

    """
    return Settings()
