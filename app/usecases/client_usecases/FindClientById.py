from uuid import UUID

file_client = "csv/client_csv.csv"

file_pet = "csv/pet_csv.csv"


def find_client_by_id(client_id: UUID):
    # Busca o cliente pelo ID
    client = None
    with open(file_client, "r") as file:
        header = next(file, None)
        if header is None:
            return {"error": "Arquivo de clientes está vazio ou sem cabeçalho."}

        for line in file:
            line = line.strip()
            if line:
                id, name, cpf, age, is_admin = line.split(",")
                if UUID(id) == client_id:
                    client = {
                        "id": id,
                        "name": name,
                        "cpf": cpf,
                        "age": age,
                        "is_admin": is_admin,
                        "pets": [],
                    }
                    break

    if not client:
        return {"error": f"Cliente com ID {client_id} não encontrado."}

    # Busca os pets associados ao cliente
    with open(file_pet, "r") as file:
        header = next(file, None)
        if header is None:
            return client  # Arquivo de pets vazio, retorna só o cliente

        for line in file:
            line = line.strip()
            if line:
                pet_data = line.split(",")
                if len(pet_data) == 4:
                    pet_id, name, breed, id_client = pet_data
                    if UUID(id_client) == client_id:
                        client["pets"].append(
                            {"id": pet_id, "name": name, "breed": breed}
                        )

    return client
