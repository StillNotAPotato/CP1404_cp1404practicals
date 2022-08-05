"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Start of subject reader program"""
    subjects = load_subjects()  # data = None
    # +----------------------
    #                       V
    display_subjects(subjects)
    total_number_of_students = get_total_number_of_students(subjects)
    # display_subjects(subjects)
    print(f"Total number of students taking {len(subjects)} subjects = {total_number_of_students}")


def display_subjects(subjects):
    """Display subject code, lecturer and number of students."""
    # CP1401 is taught by Ada Lovelace and has 192 students
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:4} students")


def get_total_number_of_students(subjects):
    """Calculate total number of students in all subjects"""
    total_students = 0
    for subject in subjects:
        total_students += subject[2]
    return total_students


def load_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []  # a list of lists (a list of subject list)
    input_file = open(FILENAME, "r")
    for line in input_file:
        # print("line", line)  # See what a line looks like
        # print("repr", repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print("parts:", parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print("parts after int(),", parts)  # See if that worked
        # print("----------")
        subjects.append(parts)  # put in the subject into a list of subjects
    input_file.close()
    # missing return statement
    return subjects  # return list of lists


main()
