import random
from prompts import PROMPTS
from utils import generate_seo_post
from openrouter_api import generate_openrouter_content

def generate_all_posts():
    posts = []
    for i in range(20):
        topic = PROMPTS[i % len(PROMPTS)]
        prompt = topic.format(app_name="Bitcoin Cloud Mining", website="https://bitcoincloudminingindia.github.io/Bitcoin-Cloud-Mining-Website/")
        raw_content = generate_openrouter_content(prompt)
        title, content = generate_seo_post(raw_content)
        posts.append((title, content))
    return posts