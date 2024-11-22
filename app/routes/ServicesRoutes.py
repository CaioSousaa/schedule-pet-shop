from fastapi import APIRouter, HTTPException, Header
from uuid import UUID
from app.usecases.services_usecases.CreateServiceUseCase import (
    create_new_services,
)
from app.usecases.services_usecases.GetAllServicesUsecase import get_all_services
from app.models.Services import Services


router = APIRouter()


@router.post("/services/create")
async def create_services_route(services: Services, user_id: UUID = Header(...)):
    try:
        create_new_services(services, user_id)
        return {"message": "Serviço criado com sucesso!"}
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/services/")
async def get_all_services_route():
    try:
        services = get_all_services()
        if not services:
            return {"msg": "Nenhum cliente encontrado"}
        return {"services": services}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao obter os serviços: {str(e)}"
        )
