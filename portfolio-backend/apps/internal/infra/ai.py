# from http.client import HTTPException
from openai import OpenAI


def factory_open_ai():
    return OpenAI()

def get_ai_response(user_message: str, model_name : str, client: OpenAI):
    if user_message == "":
        raise ValueError("userMessage cannot be empty")
    resp = client.responses.create(
        model= model_name,
        input= user_message,
    )
    return resp