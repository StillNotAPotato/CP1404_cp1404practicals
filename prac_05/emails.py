def main():
    """Create dictionary of emails to names."""
    email_to_name = {}  # email as key, name as value
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input("Is your name {}? (Y/n)".format(name))
        if confirm.upper() != "Y" and confirm != "":
            email = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def extract_name(email):
    """Get name from email address."""
    prefix = email.split("@")[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == '__main__':
    main()
