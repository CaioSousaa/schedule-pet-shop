from pydantic import BaseModel
from uuid import UUID, uuid4


class User(BaseModel):
    id: UUID = uuid4()
    name: str
    cpf: str
    age: int
    is_admin: bool
