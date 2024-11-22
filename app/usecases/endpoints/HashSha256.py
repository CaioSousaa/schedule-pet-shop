import os
import hashlib

file_csv = "csv/pet_csv.csv"
hash_SHA256 = "csv/hash.txt"


def generate_hash():
    try:
        if not os.path.exists(file_csv):
            raise FileNotFoundError("Arquivo CSV não encontrado.")

        with open(file_csv, "rb") as f:
            sha256_hash = hashlib.sha256(f.read()).hexdigest()

        with open(hash_SHA256, "w") as file:
            file.write(sha256_hash)

        print("Hash SHA256 gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao gerar Hash SHA256: {e}")
