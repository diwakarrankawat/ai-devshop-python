"""Configuration management for ai-devshop-python."""
import os

class Config:
    """Basic configuration loader for environment variables."""
    @staticmethod
    def get(key: str, default: str | None = None) -> str | None:
        """Retrieve environment variable or default."""
        return os.getenv(key, default)

