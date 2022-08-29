from guitar import Guitar


def main():
    """Test guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {98}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {7}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    main()
