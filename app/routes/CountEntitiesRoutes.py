from fastapi import APIRouter, HTTPException
from app.usecases.endpoints.CountEntities import count_entitites

router = APIRouter()


@router.get("/countEntities/")
def count_entities_pet_csv():
    try:
        quant = count_entitites()

        if not quant:
            return {"msg": "Nenhum pet encontrado"}
        return {"message": f"{quant} entidades presentes no arquivo csv."}
    except Exception as e:
        raise HTTPException(status_code=500, datail=f"Erro ao obter o pet: {str(e)}")
