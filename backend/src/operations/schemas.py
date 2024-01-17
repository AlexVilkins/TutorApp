from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    username: str
    price: int
    object: str
    hour: datetime
