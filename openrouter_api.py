
import os
import requests

API_KEY = os.getenv("OPENROUTER_KEY")
MODEL = "anthropic/claude-3-haiku"

def generate_openrouter_content(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]
