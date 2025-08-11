# from http.client import HTTPException
from openai import OpenAI, APIStatusError


def factory_open_ai():
    # ローカルでは環境変数に設定されてあるため、セットは不要
    return OpenAI()

def factory_open_ai_set_key(key):
    return OpenAI(api_key=key)

def get_ai_response(user_message: str, model_name : str, client: OpenAI) -> str | int:
    if user_message == "":
        raise ValueError("userMessage cannot be empty")
    try:
        resp = client.responses.create(
            model=model_name,
            input=user_message,
        )
        return resp.output_text
    except APIStatusError as e:
        print(f"Error: {e}")
        return str(e.status_code)
