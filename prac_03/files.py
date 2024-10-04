"""
CP1404 - Practical 3
various file interactions
"""

name = input("Name: ")
FILENAME = "name.txt"
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

in_file = open(FILENAME, "r")
print(f"Hi, {in_file.read().strip()}!")

