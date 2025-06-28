import requests
import os

def generate_openrouter_content(prompt):
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    
    if not OPENROUTER_API_KEY:
        raise ValueError("❌ OPENROUTER_API_KEY environment variable not found. Please set it in your environment.")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "anthropic/claude-3-haiku",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        
        if "choices" not in data or not data["choices"]:
            print("❌ Unexpected response from OpenRouter API:")
            print(data)
            raise KeyError("No 'choices' found in API response")
            
        return data["choices"][0]["message"]["content"]
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        raise
    except KeyError as e:
        print("❌ Unexpected response structure from OpenRouter API:")
        print(data)
        raise
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise
