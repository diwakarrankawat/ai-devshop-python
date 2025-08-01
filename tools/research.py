import requests
from agents import function_tool
from config import Config

API_KEY = Config.get("PERPLEXITY_API_KEY")

headers = {
    "content-type": "application/json",
    "authorization": f"Bearer {API_KEY}"
}

@function_tool
def internet_search(query: str) -> str:
    """
    Search the internet for basic one-shot information.
    """
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "return_images": False,
        "return_related_questions": False,
    }

    resp = requests.post('https://api.perplexity.ai/chat/completions', headers=headers, json=payload)
    data = resp.json()
    message = data["choices"][0]["message"]["content"]
    return message + "\n\nSources:\n" + '\n'.join(data['citations'])

@function_tool
def internet_deep_search(query: str) -> str:
    """
    Search the internet for deep and detailed information.
    Must provide a detailed strategy for the search.
    """
    payload = {
        "model": "sonar-deep-research",
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "return_images": False,
        "return_related_questions": False,
    }

    resp = requests.post('https://api.perplexity.ai/chat/completions', headers=headers, json=payload)
    data = resp.json()
    message = data["choices"][0]["message"]["content"]
    return message + "\n\nSources:\n" + '\n'.join(data['citations'])

@function_tool
def internet_reasoned_search(query: str) -> str:
    """
    Search the internet and reason about the information.
    Must provide a detailed query.
    """
    payload = {
        "model": "sonar-reasoning",
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "return_images": False,
        "return_related_questions": False,
    }

    resp = requests.post('https://api.perplexity.ai/chat/completions', headers=headers, json=payload)
    data = resp.json()
    message = data["choices"][0]["message"]["content"]
    # return message + "\n\nSources:\n" + '\n'.join(data['citations'])
    return message
