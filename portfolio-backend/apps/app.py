from fastapi import FastAPI
from fastapi import Request
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

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
    return {"message": body["message"]}

lambda_handler = Mangum(app)