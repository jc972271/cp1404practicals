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
    """Manage the calling of a user selected menu option."""
    score = get_score()
    choice = menu()
    while choice != 'Q':
        if choice == 'G':
            score = get_score()
        elif choice == 'P':
            evaluation = evaluate_score(score)
            print(evaluation)
        elif choice == 'S':
            print_string(score)
        else:
            print("Invalid choice")
        choice = menu()
    print("Goodbye")


def menu():
    """Print the menu layout."""
    print_string(50, "-")
    print(MENU)
    choice = input(">>> ").upper()
    print_string(50, "-")
    return choice


def print_string(amount, string="*"):
    """Print a multiplied string."""
    print(string * amount)


def get_score():
    """Get score input from a user."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def evaluate_score(score):
    """Evaluate a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
