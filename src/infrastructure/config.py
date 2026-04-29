"""
Configurações globais da aplicação.
Carrega variáveis de ambiente via Pydantic BaseSettings (pydantic-settings),
instancia o rate limiter (slowapi) e expõe o objeto `settings` como ponto
único de acesso às variáveis de ambiente em todo o projeto.
"""
import dotenv
import os
from pydantic_settings import BaseSettings
from slowapi import Limiter
from slowapi.util import get_remote_address

dotenv.load_dotenv()

class Settings(BaseSettings):
    AI_API_KEY: str
    AI_MODEL: str
    APP_NAME: str = "AI-ChatBot"
    RUN_MODE: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DATA_PATH: str = "./data"
    ALLOWED_ORIGINS: list[str] = ["http://localhost"]
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()

if not os.path.exists(".initialized"):
    from src.tools.setup import run_setup
    run_setup()

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost").split(",")

LIMITER = Limiter(key_func=get_remote_address)