import os

from openai import OpenAI
from fastapi import FastAPI
from fastapi import Request
from starlette.middleware.cors import CORSMiddleware
import uvicorn

OPEN_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(value: Request):
    body = await value.json()
    request_message = body.get("message")
    resp = client.responses.create(
        model="ft:gpt-4o-mini-2024-07-18:personal::C2wLyaHP",  # 速くて安い系。必要なら他モデルへ
        input=request_message
    )
    return {"message": resp.output_text}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)