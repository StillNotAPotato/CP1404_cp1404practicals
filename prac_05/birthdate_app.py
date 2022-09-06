def main():
    name_to_date_of_birth = {}


    for i in range(5):
        name = input(f"{i+1}) Name?")
        date_of_birth = input("Birthday (dd/mm/yyyy)? ")    #string
        date_of_birth = tuple([int(x) for x in date_of_birth.split("/")
        name_to_date_of_birth[name] = date_of_birth

    print(name_to_date_of_birth)


if __name__ == '__main__':
    main()
