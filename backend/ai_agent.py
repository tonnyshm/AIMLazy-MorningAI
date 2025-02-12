import openai
import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/lazy-response")
def get_response(user_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant who is extremely lazy and sarcastic."},
            {"role": "user", "content": user_input}
        ]
    )
    return {"response": response["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)