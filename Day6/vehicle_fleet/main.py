from models import Car, Bike, Auto, SurgePricedCar


def main():
    fleet = {
        "CAR101": Car("CAR101", "Arun"),
        "BIKE201": Bike("BIKE201", "Kumar"),
        "AUTO301": Auto("AUTO301", "Ravi"),
        "SURGE401": SurgePricedCar("SURGE401", "Priya"),
    }

    distance = 10

    print("\n=== Trip Summaries ===\n")

    for vehicle in fleet.values():
        print(vehicle.trip_summary(distance))


if __name__ == "__main__":
    main()