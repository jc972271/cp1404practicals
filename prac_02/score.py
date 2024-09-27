"""
CP1404 - Practical 2
Code to determine score status
"""
from random import randint


def main():
    score = float(input("Enter score: "))
    evaluation = evaluate_score(score)
    print(evaluation)

    random_score = randint(0, 100)
    evaluation = evaluate_score(random_score)
    print("Random Score:", random_score)
    print(evaluation)

def evaluate_score(score):
    if score < 0 or score > 100:
        evaluation = "Invalid score"
    elif score >= 90:
        evaluation = "Excellent"
    elif score >= 50:
        evaluation = "Passable"
    else:
        evaluation = "Bad"
    return evaluation


main()
