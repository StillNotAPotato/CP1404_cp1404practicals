"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(grade_score(score))


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
