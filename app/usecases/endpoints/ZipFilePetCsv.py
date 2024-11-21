import os
import zipfile

PET_FILE = "csv/pet_csv.csv"
ZIP_FILE = "csv/pet_csv.zip"

def zip_csv():
    if not os.path.exists(PET_FILE):
        raise FileNotFoundError("Arquivo CSV não encontrado.")
    
    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(PET_FILE, os.path.basename(PET_FILE)) 
    
    return ZIP_FILE
