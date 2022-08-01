def main():
    password = input("Password: ")
    if 9 < len(password) or len(password) > 17:
        print("Password length should be 10 to 16 characters.")



main()
