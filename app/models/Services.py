from pydantic import BaseModel
from datetime import date

class Services(BaseModel):
    id: int
    type_service: str
    price: float
