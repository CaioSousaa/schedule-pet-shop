from fastapi import APIRouter, HTTPException
from app.usecases.pet_usecases.CreatePetUseCase import create_new_pet
from uuid import UUID

router = APIRouter()


@router.post("/pets/")
async def create_pet_route(name: str, breed: str, id_client: UUID):
    try:
        create_new_pet(name=name, breed=breed, id_client=id_client)
        return {"message": "Pet criado e salvo com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar o pet: {str(e)}")
