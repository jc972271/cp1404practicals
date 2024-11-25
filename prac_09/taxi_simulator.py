"""
CP1404 - Practical 9
Simulate chosen taxis and the cost of the trip
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    """Manages the menu."""
    chosen_taxi = None
    total_bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            chosen_taxi = choose_taxi(taxis)
        elif choice == "D":
            if chosen_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(chosen_taxi)
        else:
            print("Invalid choice")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


def drive_taxi(chosen_taxi):
    """Get a distance from a user and drive a taxi that distance."""
    distance = int(input("Drive how far (km)? "))
    chosen_taxi.drive(distance)
    fare = chosen_taxi.get_fare()
    chosen_taxi.start_fare()
    print(f"Your {chosen_taxi.name} trip cost you ${fare:.2f}")
    return fare


def choose_taxi(taxis):
    """Get a user to choose a taxi from a list."""
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
