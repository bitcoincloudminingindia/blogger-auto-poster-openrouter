# Blogger Auto Poster

Automated blog post generator and publisher for Blogger using AI content generation.

## 🚀 Features

- 🤖 AI-powered content generation using OpenRouter (Claude-3-Haiku) and Gemini as fallback
- 📝 SEO-optimized blog posts with proper formatting
- ⏰ Automated daily posting at 9:00 AM
- 🔄 Fallback mechanism if primary API fails
- 📱 Mobile-first content for Bitcoin Cloud Mining
- ☁️ **GitHub Actions ready** - Completely free automation
- 🔒 **Security focused** - Sensitive files automatically ignored

## 📋 Prerequisites

1. **Python 3.7+**
2. **OpenRouter API Key** - Get from [https://openrouter.ai/](https://openrouter.ai/)
3. **Gemini API Key** - Get from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
4. **Google Blogger API** - `client_secret.json` file

## 🛠️ Setup

### GitHub Actions (Recommended - Free)

#### 1. Prepare Blogger Credentials
```bash
python setup_blogger_creds.py
```
This will give you a JSON string to use as `BLOGGER_CREDENTIALS`.

#### 2. Set GitHub Secrets
1. Go to your GitHub repository
2. Settings → Secrets and variables → Actions
3. Add these repository secrets:
   - `OPENROUTER_API_KEY` - Your OpenRouter API key
   - `GEMINI_API_KEY` - Your Gemini API key
   - `BLOGGER_CREDENTIALS` - The JSON string from step 1

#### 3. Push to GitHub
```bash
git add .
git commit -m "Add GitHub Actions workflow"
git push origin main
```

The workflow will automatically run daily at 9:00 AM UTC.

### Local Development

#### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2. Configure API Keys
Run the setup script:
```bash
python setup.py
```

Or manually create a `.env` file:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

#### 3. Blogger API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Blogger API v3
4. Create OAuth 2.0 credentials
5. Download `client_secret.json` and place it in the project root
6. **Important**: Rename `client_secret.example.json` to `client_secret.json` and update with your real credentials

### Render Deployment (Paid)

#### 1. Prepare Blogger Credentials
```bash
python setup_blogger_creds.py
```

#### 2. Deploy to Render
1. Push your code to GitHub
2. Connect your repository to Render
3. Create a new **Cron Job** service
4. Set the following environment variables in Render dashboard:
   - `OPENROUTER_API_KEY` - Your OpenRouter API key
   - `GEMINI_API_KEY` - Your Gemini API key
   - `BLOGGER_CREDENTIALS` - The JSON string from step 1

#### 3. Configure Render Settings
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python main.py`
- **Schedule**: `0 9 * * *` (Daily at 9:00 AM UTC)

## 🚀 Usage

### GitHub Actions (Automatic)
The application will automatically run daily at 9:00 AM UTC via GitHub Actions.

### Local Development
```bash
python main.py
```

### Manual Trigger (GitHub Actions)
1. Go to your GitHub repository
2. Actions tab
3. Select "Blogger Auto Poster" workflow
4. Click "Run workflow"

## 📁 File Structure

- `main.py` - Main application with scheduling
- `generate_posts.py` - Content generation logic
- `openrouter_api.py` - OpenRouter API integration
- `gemini_api.py` - Gemini API integration (fallback)
- `post_to_blogger.py` - Blogger publishing (Render-compatible)
- `prompts.py` - AI prompts for content generation
- `utils.py` - Utility functions
- `setup.py` - Setup script for API keys
- `setup_blogger_creds.py` - Helper for Render deployment
- `.github/workflows/blogger-auto-poster.yml` - GitHub Actions workflow
- `render.yaml` - Render configuration
- `client_secret.example.json` - Template for Blogger credentials

## 🔧 Configuration

### Blog ID
Update `BLOG_ID` in `post_to_blogger.py` with your Blogger blog ID.

### Posting Schedule
- **GitHub Actions**: Edit cron schedule in `.github/workflows/blogger-auto-poster.yml`
- **Local**: Modify the schedule in `main.py`
- **Render**: Update the cron schedule in `render.yaml`

### Content Topics
Edit `prompts.py` to customize content topics and themes.

## 🛡️ Error Handling

- Automatic fallback from OpenRouter to Gemini API
- Environment variable validation
- Network error handling
- API rate limit management
- **GitHub Actions compatible** - No browser required

## 🔐 Authentication

### Local Development
Uses `client_secret.json` and browser authentication.

### GitHub Actions & Render Deployment
Uses environment variable `BLOGGER_CREDENTIALS` with pre-authenticated tokens.

## 🔒 Security

### Protected Files
The following files are automatically ignored by Git to protect your credentials:
- `.env` - Environment variables
- `client_secret.json` - Google API credentials
- `token.pickle` - Authentication tokens
- `credentials.json` - Other API credentials

### Best Practices
1. **Never commit real credentials** to Git
2. Use environment variables for sensitive data
3. Keep `client_secret.example.json` as a template
4. Use GitHub Secrets for GitHub Actions
5. Use Render environment variables for deployment

## 💰 Cost Comparison

| Platform | Cost | Features |
|----------|------|----------|
| **GitHub Actions** | **Free** | ✅ Daily automation, Manual trigger, Reliable |
| Render Cron Job | $7/month | ✅ Daily automation, Manual trigger |
| Railway | Free tier | ✅ Limited automation |
| Heroku | Free tier | ✅ Limited automation |

## 📝 License

This project is for educational purposes. Please ensure compliance with API terms of service.
