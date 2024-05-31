from typing import List
from openai.types.chat import ChatCompletionMessageParam
from prompts.screenshot_system_prompts import get_system_prompt

USER_PROMPT = "Generate code for a web page that looks exactly like this."

def assemble_prompt(image_url: str, stack: str) -> List[ChatCompletionMessageParam]:
    system_prompt = get_system_prompt(stack)
    user_prompt = f"{USER_PROMPT} Screenshot: {image_url}. Please generate the HTML code as accurately as possible to match the screenshot."
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
