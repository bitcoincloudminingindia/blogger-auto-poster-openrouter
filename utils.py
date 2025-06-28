from datetime import datetime

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