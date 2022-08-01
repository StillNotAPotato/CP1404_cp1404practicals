"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(grade_score(score))


def grade_score(score):
    if score < 0 or score > 100:
        print("Invalid score")

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Pass"

    elif score <= 50:
        return "Bad"


main()
