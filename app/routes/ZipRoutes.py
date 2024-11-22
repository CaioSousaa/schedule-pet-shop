from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.usecases.endpoints.ZipFilePetCsv import zip_csv

router = APIRouter()


@router.get("/zip/download-zip")
async def download_pets_as_zip():
    try:
        zip_path = zip_csv()

        return FileResponse(
            path=zip_path, media_type="application/zip", filename="pet_csv.zip"
        )

    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao processar o download: {str(e)}"
        )
