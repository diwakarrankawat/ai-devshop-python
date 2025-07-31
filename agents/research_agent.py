"""Agent that leverages Perplexity tools for research."""

from tools import research


class ResearchAgent:
    """Simple agent that exposes research tools."""

    def __init__(self, model: str = "o3") -> None:
        self.model = model

    def quick_search(self, query: str) -> str:
        return research.quick_search(query)

    def deep_research(self, query: str, steps: int = 3) -> str:
        return research.deep_research(query, steps=steps)
