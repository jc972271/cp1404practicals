"""
CP1404 - Practical 3
Code for testing various file interactions
"""

name = input("Name: ")
FILENAME = "name.txt"
out_name_file = open(FILENAME, "w")
print(name, file=out_name_file)
out_name_file.close()

in_name_file = open(FILENAME, "r")
print(f"Hi, {in_name_file.read().strip()}!")
in_name_file.close()

with open("numbers.txt", "r") as numbers_file:
    x = int(numbers_file.readline())
    y = int(numbers_file.readline())
    print(x + y)

with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total = total + int(line)
    print(total)
