"""
CP1404 - Practical 1
Code for calculating total price of items
"""
total_price = 0
number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of Item: "))
    total_price = total_price + price_of_item
print(f"Total price for {number_of_items} items is {total_price:.2f}")
