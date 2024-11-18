from pydantic import BaseModel
from datetime import date
from uuid import UUID, uuid4


class Services(BaseModel):
    id: UUID = uuid4()
    id_client: UUID
    id_service: int
    date: date
