MIN_LENGTH = 8


def version_1():
    """
    Ask user to enter password, minimum 8 characters. Then print in asterisks.
    """
    password = input(f"Please enter a password of minimum {MIN_LENGTH} characters: ")
    while len(password) < 8:
        print("Password does not meet minimum length requirement")
        password = input(f"Please enter a password of minimum {MIN_LENGTH} characters: ")
    if len(password) >= 8:
        print("*" * len(password))


# version_1()


def main():
    """Ask user to enter password, minimum 8 characters. Then print in asterisks."""
    password = get_password()
    encode_password(password)


def encode_password(password):
    """Takes the length of password and print in asterisks"""
    if len(password) >= 8:
        print("*" * len(password))


def get_password():
    """Takes password and checks if it meets minimum length requirement"""
    password = input(f"Please enter a password of minimum {MIN_LENGTH} characters: ")
    while len(password) < 8:
        print("Password does not meet minimum length requirement")
        password = input(f"Please enter a password of minimum {MIN_LENGTH} characters: ")
    return password
