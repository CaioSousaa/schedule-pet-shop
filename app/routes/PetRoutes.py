from fastapi import APIRouter, HTTPException
from app.usecases.pet_usecases.CreatePetUseCase import create_new_pet
from app.usecases.pet_usecases.GetAllPets import get_all_pets
from uuid import UUID

router = APIRouter()


@router.post("/pets/create")
async def create_pet_route(name: str, breed: str, id_client: UUID):
    try:
        create_new_pet(name=name, breed=breed, id_client=id_client)
        return {"message": "Pet criado e salvo com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar o pet: {str(e)}")


@router.get("/pets/")
async def get_all_pets_route():
    try:
        pets = get_all_pets()
        if not pets:
            return {"msg": "Nenhum pet encontrado"}
        return {"pets": pets}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter os pets: {str(e)}")
