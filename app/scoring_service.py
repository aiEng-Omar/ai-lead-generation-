import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter uses an OpenAI-compatible API
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def score_lead(analysis_text: str):
    prompt = f"""
You are a lead scoring assistant.

Based on the following business analysis, give:
1. a lead score from 1 to 10
2. a short reason

Analysis:
{analysis_text}

Return plain text.
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content