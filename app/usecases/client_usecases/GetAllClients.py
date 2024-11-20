import os
from uuid import UUID
from app.models.Pet import Pet

file_client = "csv/client_csv.csv"

file_pet = "csv/pet_csv.csv"


def get_all_clients_with_pets():
    # Verifica se o arquivo de clientes existe
    if not os.path.exists(file_client):
        print("Nenhum Cliente encontrado. O arquivo ainda não foi criado.")
        return []

    clients = []

    # Lê os dados do arquivo de clientes
    with open(file_client, "r") as file:
        header = next(file, None)
        if header is None:
            print("O arquivo de clientes está vazio ou sem cabeçalho.")
            return []

        for line in file:
            line = line.strip()
            if line:
                id, name, cpf, age, is_admin = line.split(",")
                clients.append(
                    {
                        "id": id,
                        "name": name,
                        "cpf": cpf,
                        "age": age,
                        "is_admin": is_admin,
                        "pets": [],
                    }
                )

    # Verifica se o arquivo de pets existe
    if not os.path.exists(file_pet):
        print("Nenhum Pet encontrado. O arquivo ainda não foi criado.")
        return clients

    pets = []

    # Lê os dados do arquivo de pets
    with open(file_pet, "r") as file:
        header = next(file, None)
        if header is None:
            print("O arquivo de pets está vazio ou sem cabeçalho.")
            return clients

        for line in file:
            line = line.strip()
            if line:
                pet_data = line.split(",")
                if len(pet_data) == 4:
                    id, name, breed, id_client = pet_data
                    pets.append(
                        Pet(
                            id=UUID(id),
                            name=name,
                            breed=breed,
                            id_client=UUID(id_client),
                        )
                    )

    # Relaciona os pets aos clientes
    for client in clients:
        client_id = UUID(client["id"])
        client["pets"] = [
            {"id": str(pet.id), "name": pet.name, "breed": pet.breed}
            for pet in pets
            if pet.id_client == client_id
        ]

    return clients
