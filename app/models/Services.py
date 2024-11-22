from pydantic import BaseModel
from uuid import UUID, uuid4


class Services(BaseModel):
    id: UUID = uuid4()
    type_service: str
    price: float
