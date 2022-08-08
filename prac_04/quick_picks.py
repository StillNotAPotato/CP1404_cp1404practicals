MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_DIGITS_IN_LINE = 6


def main():
    number_of_picks = int(input("How many picks do you want: "))
    while number_of_picks <= 0:
        print("Got to be at least one mate")
        number_of_picks = int(input("How many picks do you want: "))




main()
