def main():
    with open("name.txt", 'r+') as name_file:
        # name_file = open("name.txt", 'r+')  # r+ is to read and write to a file
        name = input("Please enter your name: ")  # ask user to enter their name
        name_file.write(name)  # write the name to the file

        first_line = name_file.readline()  # reads the first line of the file
        print(f"Your name is {first_line}")
        name_file.close()

    total = 0
    with open("numbers.txt", 'r') as number_file:
        #   first_line = number_file.readline()
        #   second_line = number_file.readline()
        #   print(int(first_line) + int(second_line), end="")
        for line in number_file:
            line = line.strip()
            lines = line.split(',')
            for line in lines:
                total = total + int(line)   # print the sum of all the numbers in the list
    print(total)

    number_file.close()


main()
