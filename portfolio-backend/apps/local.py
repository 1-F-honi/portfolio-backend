import uvicorn
from fastapi import FastAPI
from internal.infra.cors import cors_setting
from internal.presentation import routes

app = FastAPI()
cors_setting(app)
app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run("local:app", host="0.0.0.0", port=8000, reload=True)