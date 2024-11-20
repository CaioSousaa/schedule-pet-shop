from uuid import UUID
import os

FILE = "csv/pet_csv.csv"

def delete_pet_by_id(id: UUID) -> bool:
    if not os.path.exists(FILE):
        print("O arquivo não existe.")
        return False

    pet_found = False
    remaining_lines = []

    with open(FILE, "r") as file:
        header = next(file) 
        remaining_lines.append(header.strip())  

        for line in file:
            line = line.strip()
            if line:
                pet_id, name, breed, id_client = line.split(",")
                if pet_id == str(id): 
                    pet_found = True
                    continue  
                remaining_lines.append(line)

    if pet_found:
        with open(FILE, "w") as file:
            file.write("\n".join(remaining_lines) + "\n")
        print(f"Pet com ID {id} deletado com sucesso!")
        return True
    else:
        print(f"Pet com ID {id} não encontrado.")
        return False
