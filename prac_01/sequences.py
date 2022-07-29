def main():

    MENU = """Number sequence generator
    E - show even numbers from x to y
    O - show odd numbers from x to y
    S - show the squares from x to y 
    Q - exit the program
    R - reset starting & ending numbers
    """
    print(MENU)

    x = int(input("Starting number x: "))
    y = int(input("Ending number y: "))
    choice = input(">>>").upper()
    # even number: no remainder
    # odd number: have remainder

    while choice != "Q":
        if choice == "E":
            for i in range(x, y):
                if i % 2 == 0:
                    print(i, end=" ")
                print()

        elif choice == "O":
            for i in range(x, y):
                if i % 2 != 0:
                    print(i)

        elif choice == "S":
            for x in range(y):
                print(x, end=" ")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()
    # x and y are inputs
    # show even numbers from x to y
    # show odd numbers from x to y
    # show the squares from x to y
# TODO: add in fourth condition to reset the program, asking the user to give x & y value again
# TODO: add in test case where user enters the same number for x & y



main()
