import base64
from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from typing import List
import httpx
from image_generation import bytes_to_data_url

router = APIRouter()

class ScreenshotResponse(BaseModel):
    url: str

@router.post("/api/screenshot", response_model=ScreenshotResponse)
async def upload_screenshot(file: UploadFile = File(...)):
    contents = await file.read()
    mime_type = file.content_type
    data_url = bytes_to_data_url(contents, mime_type)
    return ScreenshotResponse(url=data_url)
