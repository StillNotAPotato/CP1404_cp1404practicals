def main():
    name_to_date_of_birth = {}
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12,4,1999), (1, 1, 2000), (27,3,2)]

    name_to_date_of_birth = convert_lists_to_dictionary(names, dates_of_birth)

        name = input(f"{i + 1}) Name?")
        date_of_birth = input("Birthday (dd/mm/yyyy)? ")  # string
        date_of_birth = tuple([int(x) for x in date_of_birth.split("/")
        name_to_date_of_birth[name] = date_of_birth

        print(name_to_date_of_birth)

        if __name__ == '__main__':
            main()
