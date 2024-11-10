"""
CP1404 - Practical - Extension
Code for estimating an electricity bill
"""

MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program"""
print(MENU)
choice = input(">>> ")
while choice != "4":
    if choice == "1":
        print("Find even numbers between x and y")
        x = int(input("Input start value: "))
        if (x % 2) != 0:
            x = x+1
        y = int(input("Input end value: "))
        for i in range(x, y+1, 2):
            print(i, end=' ')
        print()
    elif choice == "2":
        print("Find odd numbers between x and y")
        x = int(input("Input start value: "))
        if (x % 2) == 0:
            x = x+1
        y = int(input("Input end value: "))
        for i in range(x, y+1, 2):
            print(i, end=' ')
        print()
    elif choice == "3":
        print("Find squares of the numbers from x to y")
        x = int(input("Input start value: "))
        y = int(input("Input end value: "))
        for i in range(x, y+1, 1):
            print(i*i, end=' ')
        print()
    print(MENU)
    choice = input(">>> ")
print("Finished.")