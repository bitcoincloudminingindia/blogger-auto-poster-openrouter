#!/usr/bin/env python3
"""
Setup script for Blogger Auto Poster
This script helps you configure your API keys
"""

import os

def create_env_file():
    """Create .env file with user input"""
    print("🚀 Blogger Auto Poster Setup")
    print("=" * 40)
    print()
    
    print("You need to provide API keys for content generation:")
    print()
    
    # OpenRouter API Key
    print("1. OpenRouter API Key")
    print("   - Visit: https://openrouter.ai/")
    print("   - Sign up and get your API key")
    print("   - This will be used as primary content generator")
    openrouter_key = input("   Enter your OpenRouter API key: ").strip()
    
    print()
    
    # Gemini API Key
    print("2. Gemini API Key (Backup)")
    print("   - Visit: https://makersuite.google.com/app/apikey")
    print("   - Create a new API key")
    print("   - This will be used as fallback if OpenRouter fails")
    gemini_key = input("   Enter your Gemini API key: ").strip()
    
    print()
    
    # Create .env file
    env_content = f"""# OpenRouter API Key - Get from https://openrouter.ai/
OPENROUTER_API_KEY={openrouter_key}

# Gemini API Key - Get from https://makersuite.google.com/app/apikey
GEMINI_API_KEY={gemini_key}

# Blogger API credentials are handled via client_secret.json and token.pickle
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
        print("✅ Your API keys are now configured.")
        print()
        print("Next steps:")
        print("1. Make sure you have client_secret.json for Blogger API")
        print("2. Run: python main.py")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def show_manual_instructions():
    """Show manual setup instructions"""
    print("📝 Manual Setup Instructions:")
    print("=" * 40)
    print()
    print("1. Create a file named '.env' in the project root")
    print("2. Add the following content:")
    print()
    print("OPENROUTER_API_KEY=your_openrouter_api_key_here")
    print("GEMINI_API_KEY=your_gemini_api_key_here")
    print()
    print("3. Replace 'your_api_key_here' with your actual API keys")
    print("4. Save the file")
    print("5. Run: python main.py")

if __name__ == "__main__":
    try:
        create_env_file()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        print()
        show_manual_instructions()
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        print()
        show_manual_instructions() 