"""
CP1404 - Practical 4
Code for practicing lists
"""

numbers = []

for i in range(1, 6):
    numbers.append(int(input("Number: ")))

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[len(numbers) - 1]}")
print(f"The lowest number is {min(numbers)}")
print(f"The highest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / len(numbers)}")
