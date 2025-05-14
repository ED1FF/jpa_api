from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    database_url: str
    access_token_expire_minutes: int

settings = Settings()
