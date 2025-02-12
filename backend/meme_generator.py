import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_meme(text: str):
    meme_api_url = "https://api.imgflip.com/caption_image"
    params = {
        "template_id": "181913649",
        "username": os.getenv("IMGFLIP_USERNAME"),
        "password": os.getenv("IMGFLIP_PASSWORD"),
        "text0": "AI Morning Lazy",
        "text1": text
    }
    response = requests.post(meme_api_url, data=params)
    return response.json()