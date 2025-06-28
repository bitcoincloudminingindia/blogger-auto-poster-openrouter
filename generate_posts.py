import random
from prompts import PROMPTS
from utils import generate_seo_post
from openrouter_api import generate_openrouter_content

def generate_all_posts():
    posts = []
    for i in range(20):
        topic = PROMPTS[i % len(PROMPTS)]
        prompt = topic.format(app_name="Bitcoin Cloud Mining", website="https://bitcoincloudminingindia.github.io/Bitcoin-Cloud-Mining-Website/")
        
        try:
            raw_content = generate_openrouter_content(prompt)
        except Exception as e:
            print(f"❌ OpenRouter API failed: {e}")
            print("🔄 Trying Gemini API as fallback...")
            try:
                from gemini_api import generate_gemini_content
                raw_content = generate_gemini_content(prompt)
            except Exception as gemini_error:
                print(f"❌ Gemini API also failed: {gemini_error}")
                print("⚠️ Skipping this post due to API failures")
                continue
        
        title, content = generate_seo_post(raw_content)
        posts.append((title, content))
        print(f"✅ Generated post {i+1}/20: {title[:50]}...")
    
    return posts