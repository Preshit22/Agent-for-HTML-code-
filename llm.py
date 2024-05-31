from enum import Enum
from typing import Any, Awaitable, Callable, List
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionChunk
from config import OPENAI_API_KEY

class Llm(Enum):
    GPT_4_VISION = "gpt-4-vision-preview"
    GPT_4_TURBO_2024_04_09 = "gpt-4-turbo-2024-04-09"
    GPT_4O_2024_05_13 = "gpt-4o-2024-05-13"

async def stream_openai_response(
    messages: List[ChatCompletionMessageParam],
    api_key: str,
    base_url: str | None,
    model: Llm,
    callback: Callable[[str], Awaitable[None]] = None,
) -> str:
    client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    params = {
        "model": model.value,
        "messages": messages,
        "stream": True,
        "timeout": 600,
        "temperature": 0.7,  # Adjust temperature for more creative outputs
    }
    stream = await client.chat.completions.create(**params)
    full_response = ""
    async for chunk in stream:
        assert isinstance(chunk, ChatCompletionChunk)
        content = chunk.choices[0].delta.content or ""
        full_response += content
        if callback:
            await callback(content)
    await client.close()
    return full_response
