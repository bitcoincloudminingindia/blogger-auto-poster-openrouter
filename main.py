import schedule
import time
from generate_posts import generate_all_posts
from post_to_blogger import publish_posts

def job():
    print("✅ Generating and publishing blog posts...")
    posts = generate_all_posts()
    publish_posts(posts)
    print("✅ Done.")

# Schedule the job every day at 9:00 AM
schedule.every().day.at("09:00").do(job)

print("⏱ Auto-poster running daily at 9:00 AM...")
job()  # run immediately
while True:
    schedule.run_pending()
    time.sleep(60)