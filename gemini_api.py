
import google.generativeai as genai

genai.configure(api_key='AIzaSyCmXfBwITmVqJsi-1n0w2bAKOYn13Y0CYg')

def generate_gemini_content(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip()
