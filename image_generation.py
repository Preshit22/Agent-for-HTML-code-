import base64
from typing import Dict
from openai import AsyncOpenAI
from bs4 import BeautifulSoup
import asyncio

def bytes_to_data_url(image_bytes: bytes, mime_type: str) -> str:
    base64_image = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{base64_image}"

async def generate_image(prompt: str, api_key: str) -> str:
    client = AsyncOpenAI(api_key=api_key)
    image_params = {
        "model": "dall-e-3",  # Adjust model as needed
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024",
    }
    response = await client.images.generate(**image_params)
    await client.close()
    return response.data[0].url

async def generate_images(code: str, api_key: str, base_url: str | None, image_cache: Dict[str, str]) -> str:
    soup = BeautifulSoup(code, "html.parser")
    images = soup.find_all("img")
    prompts = [img.get("alt") for img in images if img["src"].startswith("https://placehold.co")]
    results = await asyncio.gather(*[generate_image(prompt, api_key) for prompt in prompts])
    mapped_image_urls = dict(zip(prompts, results))
    for img in images:
        if img["src"].startswith("https://placehold.co"):
            new_url = mapped_image_urls[img.get("alt")]
            img["src"] = new_url
    return soup.prettify()
