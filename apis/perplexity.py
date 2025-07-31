import requests
from config import Config


class PerplexityAPI:
    """Simple wrapper around the Perplexity search API."""

    BASE_URL = "https://api.perplexity.ai/search"

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or Config.get("PERPLEXITY_API_KEY")
        if not self.api_key:
            raise ValueError("PERPLEXITY_API_KEY not set")

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def search(self, query: str, depth: int = 1) -> dict:
        """Perform a search using Perplexity."""
        payload = {"q": query, "depth": depth}
        response = requests.post(self.BASE_URL, json=payload, headers=self._headers(), timeout=30)
        response.raise_for_status()
        return response.json()
