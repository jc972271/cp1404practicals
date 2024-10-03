import random

print(random.randint(5, 20))  # line 1

print(random.randrange(3, 10, 2))  # line 2

print(random.uniform(2.5, 5.5))  # line 3

# results line 1: 12 15 5 15 17 10 19 15 14 19
# smallest: 5
# largest: 20

# results line 2: 7 3 7 7 5 9 7 9 9 5
# smallest: 3
# largest: 9
# line 2 could not produce a 4 as it chooses a random number from the range

# results line 3: 5.32437746362797 3.1218985484358894 3.96767839217453 3.6122054513709996 4.494323135682122 4.89270969927782 4.200454283302818 3.965650967716723 3.2844179767678607 4.237308424363726
# smallest: 2.5
# largest: 5.5 however depending on the rounding used this could change
