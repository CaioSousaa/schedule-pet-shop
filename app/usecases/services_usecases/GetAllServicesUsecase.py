import os

FILE = "csv/services_csv.csv"


def get_all_services():
    if not os.path.exists(FILE):
        print("Nenhum Serviço encontrado. O arquivo ainda não foi criado.")
        return []

    services = []

    with open(FILE, "r") as file:
        header = next(file, None)
        if header is None:
            print("O arquivo está vazio ou sem cabeçalho.")
            return []

        for line in file:
            line = line.strip()
            if line:
                id, type_service, price = line.split(",")
                services.append(
                    {
                        "id": id,
                        "type_service": type_service,
                        "price": price,
                    }
                )

    return services
