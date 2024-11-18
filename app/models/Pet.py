from pydantic import BaseModel
from uuid import UUID, uuid4


class Pet(BaseModel):
    id: UUID = uuid4()
    name: str
    breed: str
    id_client: UUID
