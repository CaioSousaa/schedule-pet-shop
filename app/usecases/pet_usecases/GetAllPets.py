import os

FILE = "csv/pet_csv.csv"

def get_all_pets():
    if not os.path.exists(FILE):
        print("Nenhum pet encontrado. O arquivo ainda não foi criado.")
        return []

    pets = []

    with open(FILE, "r") as file:
        header = next(file, None)
        if header is None:
            print("O arquivo está vazio ou sem cabeçalho.")
            return []

        for line in file:
            line = line.strip()
            if line:
                id, name, breed, id_client = line.split(",")
                pets.append({
                    "id": id,
                    "name": name,
                    "breed": breed,
                    "id_client": id_client
                })

    return pets
