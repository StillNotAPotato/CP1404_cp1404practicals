def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Invalid denominator!")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished")

# Question 1: When will a ValueError occur?
#   If the user enters in a value that isn't an int type
# Question 2: When will a ZeroDivisionError occur?
#   If the user enters '0' for the denominator
# Question 3: Could you change the code to avoid the possibility of a ZeroDivsionError?
#   try:
#       numerator = int(input("Enter the numerator: "))
#       denominator = int(input("Enter the denominator:))
#       while denominator == 0:
#           print("Invalid denominator!")
#           denominator = int(input("Enter the denominator: "))
#       fraction = numerator / denominator
#       print(fraction)
# TODO: Adjust the code logic such that it can avoid a ValueError


main()