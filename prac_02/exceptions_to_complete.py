def main():
    finished = False
    number = 0
    while not finished:
        try:
            # TODO: this line
            number = int(input("Please enter an integer: "))
            # TODO: this line
        except ValueError:
            print("Please enter a valid integer.")
    print("Valid result is:", number)


main()
