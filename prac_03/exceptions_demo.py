"""
CP1404 - Practical 3
Answer the following questions:
1. When will a ValueError occur?
    When the inputted value is not an integer
2. When will a ZeroDivisionError occur?
    When the inputted denominator value is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, inform the user they inputted zero then allow them to try again
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")