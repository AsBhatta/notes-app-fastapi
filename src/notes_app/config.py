from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "sqlite:///./notes.db"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
