import csv
import os
from app.models.Client import User

csv_file = "csv/client_csv.csv"


def client_alread_exist(cpf: str) -> bool:
    """Verifica se o CPF já existe no arquivo CSV."""
    if not os.path.exists(csv_file):
        return False

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # Pula o cabeçalho

        for row in reader:
            if row and len(row) >= 3 and row[2] == cpf:  # Coluna CPF na posição 2
                return True

    return False


def create_new_cliente(user: User):
    try:
        # Verifica se o cabeçalho existe e é válido
        file_needs_header = True
        if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
            with open(csv_file, "r", encoding="utf-8") as file:
                first_line = file.readline().strip()
                file_needs_header = first_line != "ID,Name,CPF,Age,Is Admin"

        # Adiciona o novo usuário ao arquivo
        with open(csv_file, mode="a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

            if file_needs_header:
                writer.writerow(["ID", "Name", "CPF", "Age", "Is Admin"])

            writer.writerow([user.id, user.name, user.cpf, user.age, user.is_admin])

        print("Cliente adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")
