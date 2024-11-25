

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    chosen_taxi = None
    total_bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            chosen_taxi = choose_tax(taxis)
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

def drive_taxi(chosen_taxi):
    distance = int(input("Drive how far (km)? "))
    chosen_taxi.drive(distance)
    fare = chosen_taxi.get_fare()
    print(f"Your {chosen_taxi.name} trip cost you ${fare:.2f}")
    return fare


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