def main():

    numbers = [] # create an empty list called numbers
    for number in range(5): # for every number in
        enter_number = int(input("Enter 5 numbers >>> "))
        numbers.append(enter_number)
    print(f"The first number is, {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the number is {sum(numbers)/len(numbers)}")

    # inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    for name in usernames:
        enter_username = input("Username>>> ")
        if enter_username == name:
            print("Access granted")
        else:
            print("Access denied")
            enter_username = input("Username>>> ")


if __name__ == '__main__':
    main()