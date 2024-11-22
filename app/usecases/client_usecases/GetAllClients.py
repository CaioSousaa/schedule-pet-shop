import os

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
                id, name, cpf, age, is_admin = [
                    field.strip() for field in line.split(",")
                ]
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
            return []

        for line in file:
            line = line.strip()
            if line:
                id, name, breed, age, size_in_centimeters, id_client = [
                    field.strip() for field in line.split(",")
                ]
                pets.append(
                    {
                        "id": id,
                        "name": name,
                        "breed": breed,
                        "age": age,
                        "size_in_centimeters": size_in_centimeters,
                        "id_client": id_client,
                    }
                )

    # Relaciona os pets aos clientes
    for client in clients:
        client_id = client["id"]
        client["pets"] = [
            {
                "id": pet["id"],
                "name": pet["name"],
                "breed": pet["breed"],
                "age": pet["age"],
                "size_in_centimeters": pet["size_in_centimeters"],
            }
            for pet in pets
            if pet["id_client"] == client_id
        ]

    return clients
