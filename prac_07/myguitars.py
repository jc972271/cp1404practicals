"""
CP1404 - Practical 7
List Guitars - opens/reads a file, stores in objects of custom class
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Initialise the program."""
    guitars = []
    infile = open(FILENAME, "r")
    csv_guitars = csv.reader(infile)

    for line in csv_guitars:
        guitars.append(Guitar(line[0], int(line[1]), float(line[2])))
    infile.close()

    guitars = add_guitars(guitars)

    for guitar in sorted(guitars):
        print(guitar)

    save_guitars(guitars)


def add_guitars(guitars):
    """Get a guitar from user and append it to guitars."""
    name = input("Guitar's Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Guitar's Name: ")
    return guitars


def save_guitars(guitars):
    """Will save the guitars to a file."""
    outfile = open(FILENAME, "w")
    for guitar in guitars:
        print(repr(guitar), file=outfile)
    outfile.close()


main()
