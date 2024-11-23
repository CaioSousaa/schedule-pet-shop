import csv
import os

file_pet_csv = "csv/pet_csv.csv"


def count_entitites():
    try:
        if not os.path.exists(file_pet_csv):
            raise FileNotFoundError("Arquivo CSV não encontrado.")

        with open(file_pet_csv, "r") as file:
            entities = csv.reader(file)

            next(entities, None)

            quant = 0

            for line in entities:
                if any(cell.strip() for cell in line):
                    quant += 1

        return quant
    except Exception:
        print("Erro ao contar as entidades")
