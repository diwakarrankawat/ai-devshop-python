"""Entry point for the ai-devshop-python package."""
from config import Config


def main() -> None:
    """Simple startup routine."""
    greeting = Config.get("AIDEVSHOP_GREETING", "Welcome to AI Devshop!")
    print(greeting)


if __name__ == "__main__":
    main()
