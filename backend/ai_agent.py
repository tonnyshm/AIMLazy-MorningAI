import openai
from fastapi import FastAPI

app = FastAPI()

openai.api_key = "your-api-key"

@app.get("/lazy-response")
def get_response(user_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a lazy AI assistant."},
                  {"role": "user", "content": user_input}]
    )
    return {"response": response["choices"][0]["message"]["content"]}
