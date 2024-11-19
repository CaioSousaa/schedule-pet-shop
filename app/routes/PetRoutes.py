from fastapi import APIRouter, HTTPException
from app.usecases.pet_usecases.CreatePetUseCase import create_new_pet
from app.usecases.pet_usecases.GetAllPets import get_all_pets
from app.usecases.pet_usecases.FindPetById import find_pet_by_id
from app.usecases.pet_usecases.DeletePetUseCase import delete_pet_by_id
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


@router.get("/pets/{id}")
async def find_pet(id: UUID):
    try:
        pet = find_pet_by_id(id)

        if not pet:
            return {"msg": "Nenhum pet encontrado"}
        return pet
    except Exception as e:
        raise HTTPException(status_code=500, datail=f"Erro ao obter o pet: {str(e)}")


@router.delete("/pets/del/{id}")
async def delete_pet(id: UUID):
    try:
        delete_pet_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=500, datail=f"Erro ao obter o pet: {str(e)}")