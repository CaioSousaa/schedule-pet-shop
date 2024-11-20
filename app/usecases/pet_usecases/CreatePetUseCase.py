from app.models.Pet import Pet
from uuid import UUID
import json
import os

FILE = "csv/pet_csv.csv"
CLIENT_FILE = "csv/client_csv.csv"

def client_exists(id_client: UUID) -> bool:
    if not os.path.exists(CLIENT_FILE):
        return False
    
    with open(CLIENT_FILE, "r") as file:
        next(file)
        
        for line in file:
            client_id = line.split(",")[0]  
            if client_id == str(id_client):
                return True
    

def create_new_pet(name: str, breed: str, id_client: UUID):
    if not client_exists(id_client):
        print("Erro: Cliente não foi encontrado")
        return

    pet = Pet(name=name, breed=breed, id_client=id_client)
    
    pet_json = pet.json()

    if not os.path.exists(FILE):
        os.makedirs(os.path.dirname(FILE), exist_ok=True)
        
        with open(FILE, "w") as f:
            f.write("id,name,breed,id_client\n")

    with open(FILE, "a") as f:
        pet_dict = json.loads(pet_json)
        f.write(f"{pet_dict['id']},{pet_dict['name']},{pet_dict['breed']},{pet_dict['id_client']}\n")

    print("Pet criado com sucesso!")
