from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    ## These are not hardcoded. These are fallbacks that only apply when env var not set.
    env: str = "local"
    database_url: str = "postgres+psycopg://nrl:nrl@localhost:5432/nrl"
    log_level:str = "INFO"

settings = Settings()
    