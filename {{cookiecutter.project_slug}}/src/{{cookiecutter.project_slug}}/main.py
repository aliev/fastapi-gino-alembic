from fastapi import FastAPI
from .config import settings
from .db import gino
from .router import router


app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(router)
gino.init_app(app)
