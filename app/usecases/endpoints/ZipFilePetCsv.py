import os
import io
import zipfile

PET_FILE = "csv/pet_csv.csv"


def create_zip_in_memory():
    if not os.path.exists(PET_FILE):
        raise FileNotFoundError("Arquivo CSV não encontrado.")

    memory_file = io.BytesIO()
    with zipfile.ZipFile(
        memory_file, mode="w", compression=zipfile.ZIP_DEFLATED
    ) as zipf:
        zipf.write(PET_FILE, os.path.basename(PET_FILE))

    memory_file.seek(0)
    return memory_file
