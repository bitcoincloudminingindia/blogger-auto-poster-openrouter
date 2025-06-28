import os
from google.generativeai.generative_models import GenerativeModel
from google.generativeai.client import configure

# ✅ Load API key securely from environment variable
configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_gemini_content(prompt):
    model = GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip() 