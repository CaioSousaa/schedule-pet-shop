from pydantic import BaseModel
from uuid import UUID, uuid4


class Schedule(BaseModel):
    id: UUID = uuid4()
    id_client: UUID
    id_service: int
    date: date
