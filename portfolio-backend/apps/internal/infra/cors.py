from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

ALLOWED_ORIGIN = "https://1-f-honi.github.io"

def cors_setting(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[ALLOWED_ORIGIN],
        allow_methods=["POST", "OPTIONS"],  # 使うメソッドを列挙
        allow_headers=["Content-Type", "Authorization"],
    )
    return