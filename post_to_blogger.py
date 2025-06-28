import os
import pickle
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Blogger API constants
SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRET_FILE = 'client_secret.json'  # Make sure this file is present
BLOG_ID = '8249457453104091983'  # Replace with your actual blog ID

def authenticate_blogger():
    """
    Authenticate the Blogger API using OAuth 2.0.
    If token.pickle exists, it reuses it.
    If not, it opens the console flow and saves a token.
    """
    creds = None

    # Load existing token if available
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If no valid token, start OAuth console flow (Render compatible)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_console()  # type: ignore  ✅ Safe to use even if Pyright complains

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('blogger', 'v3', credentials=creds)

def publish_posts(posts):
    """
    Publishes a list of (title, content) tuples to Blogger.
    Waits 1 hour between posts to avoid API limits.
    """
    service = authenticate_blogger()

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
