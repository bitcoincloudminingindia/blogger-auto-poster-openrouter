import schedule
import time
import os
from dotenv import load_dotenv
from generate_posts import generate_all_posts
from post_to_blogger import publish_posts
from utils import check_environment_variables

# Load environment variables from .env file (for local development)
load_dotenv()

def job():
    print("🚀 Starting Blogger Auto Poster job...")
    print("=" * 50)
    
    try:
        # Check environment variables
        if not check_environment_variables():
            print("❌ Environment variables check failed")
            return
        
        print("✅ Generating blog posts...")
        posts = generate_all_posts()
        
        if posts:
            print(f"✅ Generated {len(posts)} posts successfully")
            print("📝 Publishing posts to Blogger...")
            publish_posts(posts)
            print("🎉 All posts published successfully!")
        else:
            print("⚠️ No posts were generated successfully.")
            
    except Exception as e:
        print(f"❌ Error in job execution: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("🤖 Blogger Auto Poster")
    print("=" * 30)
    print()
    
    # Check environment variables before starting
    if not check_environment_variables():
        print("❌ Exiting due to missing environment variables.")
        print("💡 Please set the required environment variables in Render dashboard:")
        print("   - OPENROUTER_API_KEY")
        print("   - GEMINI_API_KEY") 
        print("   - BLOGGER_CREDENTIALS")
        return
    
    # For Render cron jobs, run once and exit
    if os.getenv('RENDER'):
        print("🌐 Running on Render - executing job once...")
        job()
        print("✅ Job completed successfully!")
        return
    
    # For local development, run with scheduling
    print("🏠 Running locally - scheduling daily job at 9:00 AM...")
    schedule.every().day.at("09:00").do(job)
    
    print("⏱ Auto-poster running daily at 9:00 AM...")
    job()  # run immediately
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()