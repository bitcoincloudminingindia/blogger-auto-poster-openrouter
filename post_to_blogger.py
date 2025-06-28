import os
import pickle
import time
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Blogger API constants
SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRET_FILE = 'client_secret.json'
BLOG_ID = '8249457453104091983'  # Replace with your actual blog ID

def authenticate_blogger():
    """Authenticate with Blogger API using service account or stored credentials"""
    creds = None
    
    # Check if we have stored credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If we have valid credentials, use them
    if creds and creds.valid:
        return build('blogger', 'v3', credentials=creds)
    
    # If credentials are expired, refresh them
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
            return build('blogger', 'v3', credentials=creds)
        except Exception as e:
            print(f"❌ Error refreshing credentials: {e}")
    
    # For Render deployment, use environment variables for credentials
    blogger_creds = os.getenv('BLOGGER_CREDENTIALS')
    if blogger_creds:
        try:
            # Parse credentials from environment variable
            creds_data = json.loads(blogger_creds)
            creds = Credentials.from_authorized_user_info(creds_data, SCOPES)
            
            # Save credentials for future use
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
            
            return build('blogger', 'v3', credentials=creds)
        except Exception as e:
            print(f"❌ Error loading credentials from environment: {e}")
    
    # Fallback to local authentication (for development)
    if os.path.exists(CLIENT_SECRET_FILE):
        try:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
            return build('blogger', 'v3', credentials=creds)
        except Exception as e:
            print(f"❌ Error with local authentication: {e}")
    
    raise Exception("❌ No valid authentication method found. Please set BLOGGER_CREDENTIALS environment variable or provide client_secret.json")

def publish_posts(posts):
    """
    Publishes a list of (title, content) tuples to Blogger.
    Waits 1 hour between posts to avoid API limits.
    """
    try:
        service = authenticate_blogger()
        print("✅ Successfully authenticated with Blogger API")
        
        for index, (title, content) in enumerate(posts):
            post_body = {
                'kind': 'blogger#post',
                'title': title,
                'content': content
            }

            post = service.posts().insert(blogId=BLOG_ID, body=post_body, isDraft=False).execute()
            print(f"✅ Posted: {post['url']}")

            # Delay between posts to avoid Blogger rate limit
            if index < len(posts) - 1:
                print("⏳ Waiting 1 hour before next post...")
                time.sleep(3600)
                
    except Exception as e:
        print(f"❌ Error publishing posts: {e}")
        raise
