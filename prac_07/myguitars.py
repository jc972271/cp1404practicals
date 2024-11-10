"""
CP1404 - Practical 7
List Guitars - opens/reads a file, stores in objects of custom class
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"

guitars = []

infile = open(FILENAME, "r")
csv = csv.reader(infile)

for line in csv:
    guitars.append(Guitar(line[0], int(line[1]), float(line[2])))
infile.close()

for guitar in guitars:
    print(guitar)

