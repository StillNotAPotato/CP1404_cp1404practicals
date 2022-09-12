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

if __name__ == '__main__':
    main()
