"""
CP1404 - Practical 2
Code to determine score status with menu
"""

MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_score()
        elif choice == 'P':
            evaluation = evaluate_score(score)
            print(evaluation)
        elif choice == 'S':
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


def print_stars(amount):
    print("*" * amount)


def get_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


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
