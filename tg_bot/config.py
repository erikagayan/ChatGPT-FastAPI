"""
config.py — File for storing project configuration settings.

This file loads environment variables from .env and provides access to:
- BOT_TOKEN — Telegram bot token
- OPENAI_API_KEY — OpenAI API key for working with GPT-4
- BACKEND_URL — URL of FastAPI backend server

The file automatically loads variables from .env if they are defined there.
"""

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
BACKEND_URL = "http://localhost:8000"
