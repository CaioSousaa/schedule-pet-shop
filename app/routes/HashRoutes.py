from fastapi import APIRouter, HTTPException
from app.usecases.endpoints.HashSha256 import generate_hash

router = APIRouter()


@router.get("/hash/")
async def generate_hash_pets_csv():
    try:
        generate_hash()

        return {"message": "Hash SHA256 do arquivo gerado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
