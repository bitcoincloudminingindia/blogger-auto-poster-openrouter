#!/usr/bin/env python3
"""
Helper script to convert Blogger credentials to environment variable format
This script helps you get the BLOGGER_CREDENTIALS for Render deployment
"""

import os
import json
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRET_FILE = 'client_secret.json'

def get_blogger_credentials():
    """Get Blogger credentials and convert to JSON string for environment variable"""
    creds = None
    
    # Check if we have stored credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If credentials are expired, refresh them
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        except Exception as e:
            print(f"❌ Error refreshing credentials: {e}")
            creds = None
    
    # If no valid credentials, authenticate locally
    if not creds or not creds.valid:
        if os.path.exists(CLIENT_SECRET_FILE):
            try:
                print("🔐 Starting local authentication...")
                print("📝 Please complete the authentication in your browser")
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
                print("✅ Authentication completed successfully!")
            except Exception as e:
                print(f"❌ Error with local authentication: {e}")
                return None
        else:
            print("❌ client_secret.json not found!")
            return None
    
    # Convert credentials to JSON string with safe attribute access
    creds_dict = {
        'token': getattr(creds, 'token', None),
        'refresh_token': getattr(creds, 'refresh_token', None),
        'token_uri': getattr(creds, 'token_uri', 'https://oauth2.googleapis.com/token'),
        'client_id': getattr(creds, 'client_id', None),
        'client_secret': getattr(creds, 'client_secret', None),
        'scopes': getattr(creds, 'scopes', SCOPES)
    }
    
    # Validate required fields
    if not creds_dict['token'] or not creds_dict['refresh_token']:
        print("❌ Invalid credentials: missing token or refresh_token")
        return None
    
    return json.dumps(creds_dict)

def main():
    print("🚀 Blogger Credentials Setup for Render")
    print("=" * 50)
    print()
    
    creds_json = get_blogger_credentials()
    
    if creds_json:
        print("✅ Credentials obtained successfully!")
        print()
        print("📋 Copy this value to your Render environment variable BLOGGER_CREDENTIALS:")
        print("=" * 80)
        print(creds_json)
        print("=" * 80)
        print()
        print("💡 Instructions:")
        print("1. Go to your Render dashboard")
        print("2. Select your blogger-auto-poster service")
        print("3. Go to Environment tab")
        print("4. Add BLOGGER_CREDENTIALS with the value above")
        print("5. Deploy your service")
    else:
        print("❌ Failed to obtain credentials")

if __name__ == "__main__":
    main() 