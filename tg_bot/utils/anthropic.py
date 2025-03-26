"""
This module sends requests to Anthropic Claude and returns AI-generated responses.
It uses a synchronous client with `requests` for simplicity.
"""

import anthropic
from tg_bot.config import ANTHROPIC_API_KEY

client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)


async def chat_with_claude(prompt: str) -> str:
    """Send a message to Anthropic Claude and return the response"""
    try:
        response = await client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text if response.content else "❌ Empty response from Claude."

    except anthropic.APIError as e:
        return f"❌ API error from Anthropic: {e}"
