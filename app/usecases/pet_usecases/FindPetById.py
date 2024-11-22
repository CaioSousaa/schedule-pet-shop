from app.models.Pet import Pet
from uuid import UUID
import os

FILE = "csv/pet_csv.csv"


def find_pet_by_id(id: UUID) -> Pet | None:
    if not os.path.exists(FILE):
        return False

    with open(FILE, "r") as file:
        next(file)

        for line in file:
            line = line.strip()
            if line:
                pet_id, name, breed, age, size_in_centimeters, id_client = map(
                    str.strip, line.split(",")
                )
                if pet_id == str(id):
                    return Pet(
                        id=UUID(pet_id),
                        name=name,
                        breed=breed,
                        age=age,
                        size_in_centimeters=size_in_centimeters,
                        id_client=UUID(id_client),
                    )
        return None
