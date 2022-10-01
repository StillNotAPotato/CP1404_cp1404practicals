def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(numbers[0])
    print(numbers[-1])
    print(numbers[3])
    print(numbers[:-1])
    print(numbers[3:4])
    print(5 in numbers)
    print(7 in numbers)
    print("3" in numbers)
    print(numbers + [6, 5, 3])

    numbers[0] = "ten"
    print(numbers)
    numbers[-1] = 1
    print(numbers)
    print(numbers[3:])
    print(9 in numbers)


main()

# numbers[0] has a value of 3
# numbers[-1] has a value of 2
# numbers[3] has a value of 1
# numbers[:-1] shows value from 3, 1, 4, 1, 5, 9
# numbers[3:4] shows the value of index 3 to 4 (exclusive) which is 1
# 5 in numbers is True
# 7 in numbers is False
# "3" in numbers is False as data type in list is int
# numbers + [6, 5, 3] will return as [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
