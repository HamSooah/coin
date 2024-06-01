from pydantic import BaseSettings, Field
from typing import Optional


class Settings(BaseSettings):
    debug: bool = Field(..., env="DEBUG")

    db_engine: str = Field(..., env="DB_ENGINE")
    db_name: str = Field(..., env="DB_NAME")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")
    db_username: str = Field(..., env="DB_USERNAME")
    db_password: str = Field(..., env="DB_PASSWORD")
    db_tz: str = Field(..., env="TIMEZONE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
