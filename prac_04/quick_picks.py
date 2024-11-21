"""
CP1404 - Practical 4
Code to generate "quick picks" each line consists of 6 random numbers between 1 and 45.
"""

from random import randint

NUMBERS_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1

number_of_picks = int(input("How many quick picks do you want: "))

for i in range(number_of_picks):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = randint(MINIMUM, MAXIMUM)
        if not number in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()

    print(" ".join(f"{number:2}" for number in quick_pick))
