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

def generate_outreach(analysis: str):
    prompt = f"""
You are an expert AI sales assistant.

Based on this business analysis:

{analysis}

Write:
1. Personalized cold email
2. Friendly tone
3. Mention possible business pain points
4. Explain how AI automation can help
5. Keep it short and professional
"""



    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )


    return response.choices[0].message.content