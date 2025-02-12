import requests
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

STABLE_DIFFUSION_API_KEY = os.getenv("STABLE_DIFFUSION_API_KEY")

@app.get("/generate-meme")
def generate_meme(prompt: str):
    response = requests.post(
        "https://api.stablediffusionapi.com/v1/generate",
        json={"prompt": prompt, "api_key": STABLE_DIFFUSION_API_KEY}
    )
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
