from fastapi import APIRouter, HTTPException
from app.usecases.client_usecases.CreateClientUseCase import create_new_cliente
from app.usecases.client_usecases.CreateClientUseCase import client_alread_exist
from app.usecases.client_usecases.GetAllClients import get_all_clients_with_pets
from app.usecases.client_usecases.FindClientById import find_client_by_id
from app.usecases.client_usecases.UpdateClient import update_client
from app.usecases.client_usecases.DeleteClientUseCase import delete_client_by_id
from app.models.Client import User
from uuid import UUID

router = APIRouter()


@router.post("/users/create")
async def create_client_route(user: User):
    try:
        # Verifica se o CPF já existe
        if client_alread_exist(user.cpf):
            raise HTTPException(
                status_code=409, detail=f"Cliente com CPF {user.cpf} já existe."
            )

        create_new_cliente(user)
        return {"message": "Cliente criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/")
async def get_all_clients_route():
    try:
        clients = get_all_clients_with_pets()
        if not clients:
            return {"msg": "Nenhum cliente encontrado"}
        return {"clients": clients}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao obter os Clientes: {str(e)}"
        )


@router.get("/clients/{id}")
def find_client(id: UUID):
    try:
        clients = find_client_by_id(id)
        if not clients:
            return {"msg": "Nenhum cliente encontrado"}
        return {"clients": clients}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao obter o Cliente: {str(e)}"
        )


@router.put("/clients/update/{id}")
async def update(id: UUID, new_name: str, new_cpf: str, new_age: int):
    try:
        success = update_client(
            id=id, new_name=new_name, new_cpf=new_cpf, new_age=new_age
        )

        if success:
            return {"message": f"Cliente com ID {id} atualizado com sucesso."}
        else:
            raise HTTPException(
                status_code=404, detail=f"Cliente com ID {id} não encontrado."
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao realizar a alteração no Cliente: {str(e)}"
        )


@router.delete("/clients/delete/{id}")
async def delete_client(id: UUID):
    try:
        delete_client_by_id(id)
        return {"message": f"Cliente com o ID {id} deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, datail=f"Erro ao obter o pet: {str(e)}")
