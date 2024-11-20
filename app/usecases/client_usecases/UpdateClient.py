from uuid import UUID
import os

file_client = "csv/client_csv.csv"


def update_client(id: UUID, new_name: str, new_cpf: str, new_age: int) -> bool:
    if not os.path.exists(file_client):
        print("O arquivo não existe.")
        return False

    client_found = False
    updated_lines = []

    with open(file_client, "r") as file:
        header = next(file)
        updated_lines.append(header.strip())

        for line in file:
            line = line.strip()
            if line:
                client_id, name, cpf, age, is_admin = line.split(",")
                if client_id == str(id):
                    client_found = True
                    updated_lines.append(
                        f"{client_id},{new_name},{new_cpf},{new_age},{is_admin}"
                    )
                else:
                    updated_lines.append(line)

    if client_found:
        with open(file_client, "w") as file:
            file.write("\n".join(updated_lines) + "\n")
        print(f"Cliente com ID {id} atualizado com sucesso!")
        return True
    else:
        print(f"Cliente com ID {id} não encontrado.")
        return False
