from app.usecases.schedule_usecases.GetAllSchedules import get_all_schedule
from app.usecases.schedule_usecases.CreateSchedule import create_schedule
from fastapi import APIRouter, HTTPException
from datetime import date
from uuid import UUID


router = APIRouter()

@router.post("/schedule")
async def create_schedule_routes(service_id: int, client_id: UUID, date_schedule: date):
    try:
        create_schedule(service_id=service_id, client_id=client_id, date_schedule=date_schedule)
        return {"msg": "Agendamento criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar o agendamento: {str(e)}")

@router.get("/schedule/all")
async def get_all():
    try:
        schedules = get_all_schedule()
        if not schedules:
            return {"msg":"nenhum agendamento  registrado"}
        return schedules
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter os agendamentos: {str(e)}")