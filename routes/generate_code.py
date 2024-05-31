import os
import traceback
from fastapi import APIRouter, HTTPException, UploadFile, File
from config import OPENAI_API_KEY
from llm import Llm, stream_openai_response
from image_generation import generate_images, bytes_to_data_url
from prompts import assemble_prompt
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/generate-code")
async def generate_code(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        mime_type = file.content_type

        # Log the file content and type
        logger.info(f"Received file of type: {mime_type}")
        logger.info(f"File content size: {len(contents)} bytes")

        image_url = bytes_to_data_url(contents, mime_type)
        
        # Log the generated data URL
        logger.info(f"Generated data URL: {image_url[:100]}...")  # Log the first 100 characters

        prompt_messages = assemble_prompt(image_url, "html_tailwind")
        
        # Log the prompt
        logger.info(f"Prompt messages: {prompt_messages}")

        completion = await stream_openai_response(
            messages=prompt_messages,
            api_key=OPENAI_API_KEY,
            base_url=None,
            model=Llm.GPT_4O_2024_05_13,
        )

        # Log the completion
        logger.info(f"Model completion: {completion}")

        updated_html = await generate_images(completion, OPENAI_API_KEY, None, {})

        return {
            "generated_code": updated_html,
            "output_html": updated_html,
        }
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
