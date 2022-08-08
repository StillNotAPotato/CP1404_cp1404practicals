import random

MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_DIGITS_IN_LINE = 6


def main():
    global quick_pick
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Got to be at least one mate")
        number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_pick = []     # list to store the digits for the pick
        for j in range(NUMBER_OF_DIGITS_IN_LINE):
            number = random.randint(MINIMUM, MAXIMUM)     # for every iteration, number is assigned any value from
            # 1 to 45
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
                quick_pick.append(number)   # add to the quick pick list
            quick_pick.sort()   # sort the numbers in ascending order

            print(f"{number}" for number in quick_pick)


main()
