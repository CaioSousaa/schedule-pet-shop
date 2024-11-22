import os
import csv
from uuid import UUID
from app.models.Services import Services

file_services_csv = "csv/services_csv.csv"

file_client_csv = "csv/client_csv.csv"


def is_admin(user_id: UUID) -> bool:
    if not os.path.exists(file_client_csv):
        return False

    with open(file_client_csv, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if UUID(row["id"]) == user_id and row["Is Admin"].strip().lower() == "true":
                return True
    return False


def create_new_services(service: Services, user_id: UUID):
    try:
        if not is_admin(user_id):
            raise PermissionError("Usuário não possui permissão para criar serviços.")

        # Verifica se o arquivo já existe e possui dados
        file_needs_header = not os.path.exists(file_services_csv) or os.path.getsize(file_services_csv) == 0

        # Escreve no arquivo CSV
        with open(file_services_csv, mode="a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

            # Escreve o cabeçalho se necessário
            if file_needs_header:
                writer.writerow(["ID", "type_service", "price"])

            # Escreve os dados do serviço
            writer.writerow([str(service.id), service.type_service, service.price])

        print("Serviço adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar o serviço: {e}")
        raise

