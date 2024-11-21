from pydantic import BaseModel
from uuid import UUID, uuid4


class Pet(BaseModel):
    id: UUID = uuid4()
    name: str
    breed: str
    age: int
    size_in_centimeters: int
    id_client: UUID
