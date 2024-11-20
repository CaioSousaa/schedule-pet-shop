from uuid import UUID
import os

FILE = "csv/client_csv.csv"


def delete_client_by_id(id: UUID) -> bool:
    if not os.path.exists(FILE):
        print("O arquivo não existe.")
        return False

    client_found = False
    remaining_lines = []

    with open(FILE, "r") as file:
        header = next(file)
        remaining_lines.append(header.strip())

        for line in file:
            line = line.strip()
            if line:
                client_id, name, cpf, age, is_admin = line.split(",")
                if client_id == str(id):
                    client_found = True
                    continue
                remaining_lines.append(line)

    if client_found:
        with open(FILE, "w") as file:
            file.write("\n".join(remaining_lines) + "\n")
        print(f"Client com ID {id} deletado com sucesso!")
        return True
    else:
        print(f"Client com ID {id} não encontrado.")
        return False
