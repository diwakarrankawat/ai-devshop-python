"""Research tools powered by Perplexity."""

from typing import List

import openai
from config import Config
from apis.perplexity import PerplexityAPI


def quick_search(query: str) -> str:
    """Return a quick answer from Perplexity."""
    api = PerplexityAPI()
    data = api.search(query, depth=1)
    return data.get("answer", "")


def deep_research(query: str, steps: int = 3) -> str:
    """Perform multi-step research using Perplexity and OpenAI."""
    api = PerplexityAPI()
    openai.api_key = Config.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not set")

    answers: List[str] = []
    current_query = query
    for _ in range(steps):
        result = api.search(current_query, depth=2)
        text = result.get("answer", "")
        answers.append(text)
        followup_prompt = (
            "Based on the following research answer, suggest a more specific follow-up query to dig deeper.\n" + text
        )
        resp = openai.chat.completions.create(
            model="o3", messages=[{"role": "user", "content": followup_prompt}]
        )
        current_query = resp.choices[0].message.content.strip()

    summary_prompt = "\n\n".join(answers) + "\n\nProvide a concise summary of the above research."
    final_resp = openai.chat.completions.create(
        model="o3", messages=[{"role": "user", "content": summary_prompt}]
    )
    return final_resp.choices[0].message.content.strip()
