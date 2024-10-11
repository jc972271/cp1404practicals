"""
CP1404 - Practical 4

"""

from random import randint

number_of_picks = int(input("How many quick picks do you want: "))
quick_picks = []

for i in range(number_of_picks):
    quick_pick = []

    while len(quick_pick) < 6:
        number = randint(1, 45)
        if not number in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    for j in range(6):
        print(f"{quick_pick[i]:>2}", end=" ")
    print()

    quick_picks.append(quick_pick)
