from taxi import Taxi
from car import Car
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """User should be able to choose from a list of available taxis
    Can choose how far they want to drive
    At the end of each trip, show them the trip cost and add it to their bill"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Lets drive!")
    print(MENU)
    menu_choice = input(">>>").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_list_of_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except:
                print("Invalid taxi choice")

        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_destination = float(input("Drive how far? "))
                current_taxi.drive(distance_to_destination)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} cost you ${trip_cost}")

                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cot: ${total_bill:.2f}")
    print("Taxis are now: ")
    display_list_of_taxis(taxis)


def display_list_of_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
