import os
from datetime import datetime

def check_environment_variables():
    """Check if required environment variables are set"""
    required_vars = {
        "OPENROUTER_API_KEY": "OpenRouter API key for content generation",
        "GEMINI_API_KEY": "Gemini API key as fallback for content generation",
        "BLOGGER_CREDENTIALS": "Blogger API credentials (JSON string) for authentication"
    }
    
    missing_vars = []
    for var, description in required_vars.items():
        if not os.getenv(var):
            missing_vars.append(f"{var} ({description})")
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n💡 Please set these environment variables before running the application.")
        print("   For Render deployment, add them in the Render dashboard.")
        return False
    
    print("✅ All required environment variables are set")
    return True

def generate_seo_post(raw_text):
    title = raw_text.strip().split("\n")[0][:60].strip("🌟 ")
    date_str = datetime.now().strftime("%B %d, %Y")
    content = f"<h2>{title}</h2>\n<p><strong>{date_str}</strong></p>\n<p>{raw_text}</p>\n\n" + CTA_HTML
    return title, content

CTA_HTML = """
<hr>
<p><strong>About Bitcoin Cloud Mining</strong></p>
<p>Bitcoin Cloud Mining is a mobile-first, secure cloud mining platform trusted by thousands.</p>
<p>👉 <a href="https://bitcoincloudminingindia.github.io/Bitcoin-Cloud-Mining-Website/" target="_blank">Visit Website</a><br>
📲 <a href="#">Download Our App</a></p>
"""