MIN_LENGTH = 8


def main():
    """
    Ask user to enter password, minimum 8 characters. Then print in asterisks.
    """
    password = input(f"Please enter a password of minimum {MIN_LENGTH} characters: ")
    while len(password) < 8:
        print("Password does not meet minimum length requirement")
        password = input(f"Please enter a password of minimum {MIN_LENGTH} characters: ")
    if len(password) >= 8:
        print("*" * len(password))


main()
