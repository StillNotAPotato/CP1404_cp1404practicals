"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(grade_score(score))
    random_score = random.randint(0, 100)
    print(random_score)
    print(f"Random score grade is: {random_score_grader(random_score)}")


def random_score_grader(random_score):
    """Categorise the randomly generated score"""
    if random_score >= 90:
        return "Excellent"
    elif random_score >= 50:
        return "Pass"
    else:
        return "Bad"


def grade_score(score):
    """Takes user's score and categorises it"""
    if score < 0 or score > 100:
        print("Invalid score")

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Pass"

    else:
        return "Bad"


main()
