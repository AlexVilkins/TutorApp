from datetime import datetime

from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    id: int
    username: str
    price: int
    object: str
    hour: datetime
