def main():
names = []
dates_of_birth = []
names, dates_of_birth = load_names_and_birthdays("birthdays.csv")

def load_names_and_birthdays(filename):
"""Return parrallel lists of names and birthday tuples."""
names = []
dates_of_birth = []

with open("birthdays.csv", 'r') as in_file:
lines = in_file.readlines()
for line in lines:
data = line.split(",")  # data[0] -> name, data[1] -> dd/mm/yyyy            names.append(data[0])
names.append(data[0])
# birthday = tuple([int(x) for x in data[1].split("/")])
birthday = get_birthday_tuple(birthday)
dates_of_birth.append(birthday)

return names, dates_of_birth

def get_birthday_tuple(birthday):
"""Return birthday in a tuple of integers (dd, mm, yyyy."""

return tuple([int(x) for x in data[1].split("/")])

def convert_lists_to_dictionary(keys, values):
# put doc strings for all functions including main
# difficult to read code, add comment to explain what you're trying to do
# functions should only accept input, NO OUTPUTS!!!