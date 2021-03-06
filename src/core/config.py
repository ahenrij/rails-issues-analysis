"""Settings."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Package settings from .env file.
    This class looks for defined environments variables named after its variables and load their values.
    The .env file is considered by default.
    Args:
        BaseSettings (pydantic.BaseSettings): Base settings to override
    Raises
        ValueError: if something is wrong with .env file
    """

    BASE_URL: str
    GITHUB_OAUTH_TOKEN: str
    RAW_DATA_FILE_PATH: str
    DATA_FILE_PATH: str

    class Config:
        """Settings configs."""

        case_sensitive = True
        env_file = ".env"


settings = Settings()