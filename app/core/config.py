from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Watsonx configs
    WATSONX_API_KEY: str
    WATSONX_PROJECT_ID: str
    WATSONX_URL: str
    WATSONX_MODEL_ID: str

    # Pinecone configs
    PINECONE_API_KEY: str
    PINECONE_ENV: str
    INDEX_NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
