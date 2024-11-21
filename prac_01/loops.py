"""
CP1404 - Practical
Code to practice loops
"""

#Show all the odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()


#PART A
print("Part A")
for i in range(0, 101, 10):
    print(i, end=' ')
print()


#PART B
print("Part B")
for i in range(20, 0, -1):
    print(i, end=' ')
print()


#PART C
number_of_stars = int(input("Number of stars: "))
print("Part C")
print("*" * number_of_stars)


#PART D
print("Part D")
for i in range(1, number_of_stars + 1):
    print("*" * i)

