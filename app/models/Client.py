from pydantic import BaseModel
from typing import List
from .PetModel import Pet
from uuid import UUID, uuid4


class User(BaseModel):
    id: UUID = uuid4()
    name: str
    cpf: str
    age: int
    is_admin: bool
    pets: List[Pet]
