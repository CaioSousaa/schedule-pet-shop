from pydantic import BaseModel

class Services(BaseModel):
    id: int
    type_service: str
    price: float
