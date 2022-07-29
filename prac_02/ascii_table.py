LOWER = 33
UPPER = 127


def main():
    """Start of the program"""
    number = int(input("Ascii numbers?"))
    while not LOWER <= number <= UPPER:
        print(f"Number be between {LOWER} and {UPPER}")
        number = int(input("Ascii numbers?:"))

    for i in range(LOWER, UPPER + 1):
        print(f"{i:3} - {chr(i):<3}")


main()
