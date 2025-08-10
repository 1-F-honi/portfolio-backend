# from http.client import HTTPException
from openai import OpenAI


def factory_open_ai():
    # ローカルでは環境変数に設定されてあるため、セットは不要
    return OpenAI()

def factory_open_ai_set_key(key):
    return OpenAI(api_key=key)

def get_ai_response(user_message: str, model_name : str, client: OpenAI):
    if user_message == "":
        raise ValueError("userMessage cannot be empty")
    resp = client.responses.create(
        model= model_name,
        input= user_message,
    )
    return resp