import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "default")
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    LLM_MODEL_ID: str = os.getenv("LLM_MODEL_ID", "default3.1")

    MAX_PROMPT_LENGTH: int = os.getenv("MAX_PROMPT_LENGTH", 3000)


settings = Settings()
