from fastapi import FastAPI, APIRouter
from fastapi import Request
from ..infra.config import ai_config_setting
from ..infra.ai import factory_open_ai, get_ai_response

router = APIRouter()
ai_config = ai_config_setting()
ai = factory_open_ai()

@router.post("/api/chat")
async def chat(value: Request):
    body = await value.json()
    message = body["message"]
    response = get_ai_response(message, ai_config.model_name, ai)
    return {"message": response.output_text}