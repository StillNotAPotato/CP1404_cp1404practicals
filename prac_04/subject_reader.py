"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(display_data())


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    # print(parts)  # See what the parts look like (notice the integer is a string)
    # print(parts)  # See if that worked
    # list_of_parts = [parts for i in range(1)]

    # print("----------")
    input_file.close()
    return data


# CP1401 is taught by Ada Lovelace and has 192 students
# Cp1404 is taught by Alan Turing and has 98 students
def display_data():
    all_subjects = ""
    subjects = get_data()
    for subject in subjects:
        subject_code = subject[0]
        subject_teacher = subject[1]
        number_of_students = subject[2]
        all_subjects = all_subjects + f"{subject_code} is taught by {subject_teacher} and has {number_of_students} students\n "
    return all_subjects


def alice():
    candy = ['a', 'b', 'c']
    return candy


def bob():
    candy = [1]
    return candy


def all_candy():
    candy = bob()
    print(f"Bob has {candy} candies")
    candy = alice()
    print(f"Alice has {candy} candies")


def message():
    greeting = 'hello'
    return greeting


def say():
    print(message())
    greeting = 'world'
    print(greeting)


if __name__ == '__main__':
    main()
