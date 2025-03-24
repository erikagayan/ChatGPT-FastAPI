"""
This module sends requests to Anthropic Claude and returns AI-generated responses.
It uses a synchronous client with `requests` for simplicity.
"""

import os
import anthropic
from tg_bot.config import ANTHROPIC_API_KEY

# Создаем асинхронный клиент Anthropic
client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)


async def chat_with_claude(prompt: str) -> str:
    """Send a message to Anthropic Claude and return the response"""
    try:
        print(f"📤 Sending request to Claude: {prompt}")
        response = await client.messages.create(
            model="claude-3-haiku-20240307",  # Убедись, что модель правильная
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        print(f"✅ API Response: {response}")

        # Проверяем, есть ли ответ от Claude
        return response.content[0].text if response.content else "❌ Empty response from Claude."

    except anthropic.APIError as e:
        return f"❌ API error from Anthropic: {e}"
