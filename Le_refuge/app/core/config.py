from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Configuration de base pour l'application."""
    APP_NAME: str = "Le Refuge"
    DEBUG: bool = True
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """Retourne les paramètres de l'application."""
    return Settings() 