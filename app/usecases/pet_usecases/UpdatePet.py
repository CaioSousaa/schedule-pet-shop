from uuid import UUID
import os

FILE = "csv/pet_csv.csv"


def update_pet(id: UUID, new_name: str, new_id_client: UUID) -> bool:
    if not os.path.exists(FILE):
        print("O arquivo não existe.")
        return False

    pet_found = False
    updated_lines = []

    with open(FILE, "r") as file:
        header = next(file)
        updated_lines.append(header.strip())

        for line in file:
            line = line.strip()
            if line:
                pet_id, name, breed, id_client = line.split(",")
                if pet_id == str(id):
                    pet_found = True
                    updated_lines.append(f"{pet_id},{new_name},{breed},{new_id_client}")
                else:
                    updated_lines.append(line)

    if pet_found:
        with open(FILE, "w") as file:
            file.write("\n".join(updated_lines) + "\n")
        print(f"Pet com ID {id} atualizado com sucesso!")
        return True
    else:
        print(f"Pet com ID {id} não encontrado.")
        return False
