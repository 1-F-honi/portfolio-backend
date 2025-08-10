import os


class Config:
    def __init__(self):
        self.model_name: str = os.environ.get("OPENAI_API_MODEL_NAME", "")

def ai_config_setting() -> Config:
    if not os.environ.get("OPENAI_API_KEY"):
        raise Exception("OPENAI_API_KEY must be set")
    if not os.environ.get("OPENAI_API_MODEL_NAME"):
        raise Exception("OPENAI_API_MODEL_NAME must be set")
    return Config()