import os

FILE = "csv/schedule_csv.csv"


def get_all_schedule():
    if not os.path.exists(FILE):
        print("Nenhum agendamento marcado")
        return

    schedules = []

    with open(FILE, "r") as file:
        header = next(file, None)
        if header is None:
            print("O arquivo esta vazio")
            return []

        for line in file:
            line = line.strip()
            if line:
                id, id_client, id_sevice, date_schedule = line.split(",")
                schedules.append(
                    {
                        "id": id,
                        "id_client": id_client,
                        "id_service": id_sevice,
                        "date_schedule": date_schedule,
                    }
                )
    return schedules
