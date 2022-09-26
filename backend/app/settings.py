from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    db_url: PostgresDsn = "postgresql://postgres:postgres@localhost:5432/test"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
