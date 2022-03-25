from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DSN: str


settings = Settings()
