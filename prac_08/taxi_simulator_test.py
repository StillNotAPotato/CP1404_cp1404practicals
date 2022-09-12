from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    # Test Car class
    bus = Car("Mercedes", 180)
    bus.drive(30)
    print(f"fuel ={bus.fuel}")
    print(f"odometer = {bus.odometer}")
    print(bus)

    # Test drive bus
    # distance = int(input("How far? "))
    # while distance > 0:
    #   actual_distance_travelled = bus.drive(distance)
    #  print(f"{str(bus)} travelled {actual_distance_travelled}")
    #        distance = int(input("How far? "))

    # Test Taxi class
    taxi = Taxi("Hyundai i30", 100)
    print(taxi)
    taxi.drive(25)
    print(taxi, taxi.get_fare())


if __name__ == '__main__':
    main()
