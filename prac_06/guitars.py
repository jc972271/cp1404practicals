"""
CP1404 Practical 6 -
Make list of user guitars
"""
from guitar import Guitar

CURRENT_YEAR = 2024

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")
    name = input("Name: ")

max_length_name = max([len(guitar.name) for guitar in guitars])
max_length_cost = max([len(str(guitar.cost)) for guitar in guitars])

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
    print(
        f"Guitar {i}: {guitar.name:{max_length_name}} ({guitar.year}), worth ${guitar.cost:<{max_length_cost}.2f} {vintage_string}")
