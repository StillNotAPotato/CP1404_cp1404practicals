from taxi import Taxi


def main():
    # create new taxi with Prius 1, 100 units of fuel and price of $1.23/km
    taxi = Taxi("Prius 1", 120)
    # drive taxi 40km
    actual_distance_driven = taxi.drive(40)
    print(f"Taxi drove for {actual_distance_driven} km.")

    # Print taxi's details and current fare
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    # restart the meter (start new fare) and then drive 100km
    taxi.start_fare()
    actual_distance_driven = taxi.drive(100)
    print(f"Tried driving 100km, but taxi drove for {actual_distance_driven} km.")
    # print details and current fare
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
