"""
This module sends requests to GPT-4o and returns AI-generated responses.
It uses an asynchronous client to ensure non-blocking execution.
"""

import openai
from tg_bot.config import OPENAI_API_KEY

# Using OpenAI's Asynchronous Client
client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)


async def chat_with_gpt(prompt: str) -> str:
    """Send a message to GPT-4o and return the response"""
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=None,
        )
        return response.choices[0].message.content

    except openai.NotFoundError:
        return f"Error: GPT-4o model not found."

    except openai.RateLimitError:
        return f"Error: Request limit exceeded, please try again later."

    except openai.APIConnectionError:
        return f"Error: No connection to OpenAI API."

    except openai.OpenAIError as e:
        return f"Error OpenAI: {e}"
