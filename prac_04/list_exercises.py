def main():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)  # .append() is to add something to a list

    print("The first number is", numbers[0])
    print("The last number is", numbers[4])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))  # max() is to find the largest number in the arg passed into it
    print("The average of the number is", sum(numbers) / len(numbers))  # calculate sum of all numbers in the
    # list then divide by its length


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConcole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

main()
