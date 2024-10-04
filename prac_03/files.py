"""
CP1404 - Practical 3
various file interactions
"""

name = input("Name: ")
FILENAME = "name.txt"
out_file = open(FILENAME, "w")
print(name, file=out_file)

