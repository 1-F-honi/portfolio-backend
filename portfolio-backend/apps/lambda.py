from fastapi import FastAPI
from mangum import Mangum
from internal.infra.cors import cors_setting
from internal.presentation import routes

app = FastAPI()
cors_setting(app)
app.include_router(routes.router)
handler = Mangum(app)