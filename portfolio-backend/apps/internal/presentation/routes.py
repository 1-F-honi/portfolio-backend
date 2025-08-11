import os

from fastapi import APIRouter
from fastapi import Request
from ..infra.config import ai_config_setting
from ..infra.ai import factory_open_ai,factory_open_ai_set_key, get_ai_response
from ..infra.secret import get_open_ai_key

router = APIRouter()
ai_config = ai_config_setting()
# ローカル環境では環境変数からAPI_KEYを取得する
if os.environ.get("OPENAI_API_KEY") is None:
    open_api_key = get_open_ai_key()
    ai = factory_open_ai_set_key(open_api_key)
else:
    ai = factory_open_ai()

@router.post("/api/chat")
async def chat(value: Request):
    body = await value.json()
    message = body["message"]
    # エラーの時のみステータスコードを返却する
    response = get_ai_response(message, ai_config.model_name, ai)
    if isinstance(response, int):
        response = "OpenAIの連携でエラーが出ております。\nご不便をおかけし申し訳ございません。しばらくお待ちください。"
    return {"message": response}