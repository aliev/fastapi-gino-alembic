from typing import Any

from .config import settings
from gino.ext.starlette import Gino
from sqlalchemy import Column, Integer

gino = Gino(dsn=settings.DB_DSN)


class Base(gino.Model):
    id: Any = Column(Integer, primary_key=True)  # noqa
    __name__: str
    __table__: Any
