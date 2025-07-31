"""Entry point for the ai-devshop-python package."""
from config import Config
from agents import ResearchAgent


def main() -> None:
    """Simple startup routine demonstrating the research agent."""
    greeting = Config.get("AIDEVSHOP_GREETING", "Welcome to AI Devshop!")
    print(greeting)

    agent = ResearchAgent()
    query = Config.get("AIDEVSHOP_DEMO_QUERY")
    if query:
        print("Researching:", query)
        answer = agent.quick_search(query)
        print("Answer:", answer)


if __name__ == "__main__":
    main()
