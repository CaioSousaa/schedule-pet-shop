from pydantic import BaseModel


class Service(BaseModel):
    id: int
    type_service: str
    price: float
