from app.models.Schedule import Schedule
from uuid import UUID
from datetime import date
import json
import os

SCHEDULE_FILE = "csv/schedule_csv.csv"
CLIENT_FILE = "csv/client_csv.csv"
SERVICE_FILE = "csv/services_csv.csv"


def client_exists(id_client: UUID) -> bool:
    if not os.path.exists(CLIENT_FILE):
        return False

    with open(CLIENT_FILE, "r") as file:
        next(file)

        for line in file:
            client_id = line.split(",")[0]
            if client_id == str(id_client):
                return True
    return False


def services_exixts(service_id: int) -> bool:
    if not os.path.exists(SERVICE_FILE):
        return False

    with open(SERVICE_FILE, "r") as file:
        next(file)

        for line in file:
            service_id_from_file = line.split(",")[0]
            if service_id_from_file == str(service_id):
                return True
    return False


def create_schedule(service_id: int, client_id: UUID, date_schedule: date):
    if not client_exists(client_id):
        raise ValueError("Cliente não encontrado")

    if not services_exixts(service_id):
        raise ValueError("Serviço não encontrado")

    schedule = Schedule(
        id_client=client_id, id_service=service_id, date_schedule=date_schedule
    )

    schedule_json = schedule.json()

    if not os.path.exists(SCHEDULE_FILE):
        os.makedirs(os.path.dirname(SCHEDULE_FILE), exist_ok=True)

        with open(SCHEDULE_FILE, "w") as file:
            file.write("id,id_client,id_service,date_schedule\n")

    with open(SCHEDULE_FILE, "a") as file:
        schedule_dict = json.loads(schedule_json)
        file.write(
            f"{schedule_dict['id']},{schedule_dict['id_client']},{schedule_dict['id_service']},{schedule_dict['date_schedule']}\n"
        )
