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

def analyze_business(website_text: str):
    prompt = f"""
You are analyzing a business website for lead generation.

Website text:
{website_text}

Extract:
1. business type
2. main services
3. short summary
4. possible pain points
5. whether this looks like a promising lead

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