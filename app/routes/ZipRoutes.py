from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.usecases.endpoints.ZipFilePetCsv import create_zip_in_memory

router = APIRouter()

@router.get("/zip/download-zip")
async def download_pets_as_zip():
    try:
        zip_memory = create_zip_in_memory()

        return StreamingResponse(
            content=zip_memory,
            media_type="application/zip",
            headers={
                "Content-Disposition": "attachment; filename=pet_csv.zip"
            }
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o download: {str(e)}")
