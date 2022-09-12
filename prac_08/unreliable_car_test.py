from unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("DMC-12", 100, 9)
    reliable_car = UnreliableCar("Hyundai Avante CN7", 100, 90)

    for i in range(1,15):
        print(f"Attempt to drive {i}km")
        #print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2}km")
        #print(f"{unreliable_car.name:12} drove {unreliable_car.drive():2}km")
        print("{:12} drove {:2}km".format(reliable_car.name, reliable_car.drive(i)))

    print(reliable_car)
    print(unreliable_car)


if __name__ == '__main__':
    main()
