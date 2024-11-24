


MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            pass
        elif choice == "D":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

main()