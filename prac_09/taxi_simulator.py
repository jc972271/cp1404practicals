

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    chosen_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            chosen_taxi = choose_tax(taxis)
            print(type(chosen_taxi))
        elif choice == "D":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

def choose_tax(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_index = int(input("Choose Taxi: "))
        if taxi_index > len(taxis) - 1:
            print("Invalid place number")
        elif taxi_index < 0:
            print("Number must be > 0")
        else:
            return taxis[taxi_index]
    except ValueError:
        print("Invalid taxi choice")

main()