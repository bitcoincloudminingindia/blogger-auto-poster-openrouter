import os
import pickle
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRET_FILE = 'client_secret.json'
BLOG_ID = '8249457453104091983'

def authenticate_blogger():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        auth_url, _ = flow.authorization_url(prompt='consent')

        print("🔗 Please visit this URL to authorize the app:")
        print(auth_url)

        code = input("📝 Enter the authorization code here: ")
        flow.fetch_token(code=code)

        creds = flow.credentials
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('blogger', 'v3', credentials=creds)

def publish_posts(posts):
    service = authenticate_blogger()
    for index, (title, content) in enumerate(posts):
        post_body = {
            'kind': 'blogger#post',
            'title': title,
            'content': content
        }
        post = service.posts().insert(blogId=BLOG_ID, body=post_body, isDraft=False).execute()
        print(f"✅ Posted: {post['url']}")
        if index < len(posts) - 1:
            print("⏳ Waiting 1 hour before next post...")
            time.sleep(3600)
