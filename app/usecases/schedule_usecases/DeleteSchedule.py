from uuid import UUID, uuid4
import os

FILE = "csv/schedule_csv.csv"

def delete_schedule(schedule_id: UUID) -> bool:
    if not os.path.exists(FILE):
        print("O arquivo não existe.")
        return False

    schedule_found = False
    remaining_lines = []

    with open(FILE, "r") as file:
        header = next(file)
        remaining_lines.append(header.strip())

        for line in file:
            line = line.strip()
            if line:
                schedule_id, id_client, id_service, date_schedule = line.split(",")
                if schedule_id == str(schedule_id):
                    schedule_found = True
                    continue
                remaining_lines.append(line)
    
    if schedule_found:
        with open(FILE, "w") as file:
            file.write("\n".join(remaining_lines) + "\n")
        print("Agendamento excluido com sucesso!!!")
        return True
    else:
        print(f"Agendamento com ID {id} não encontrado.")
        return False