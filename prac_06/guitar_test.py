"""
CP1404 Practical 6 -
Testing the Guitar class
Estimate: 3 minutes
Actually: 3 minutes
"""
from guitar import Guitar

CURRENT_YEAR = 2024

fender = Guitar("Fender Stratocaster", 2014, 765.40)
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age(CURRENT_YEAR)}")
print(f"{fender.name} get_age() - Expected 10. Got {fender.get_age(CURRENT_YEAR)}")

print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(CURRENT_YEAR)}")
print(f"{fender.name} is_vintage() - Expected False. Got {fender.is_vintage(CURRENT_YEAR)}")
