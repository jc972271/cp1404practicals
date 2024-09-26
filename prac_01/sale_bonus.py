"""
CP1404 - Practical 1
Code for sales bonus
"""

"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

sales_amount = float(input("Enter value of sales: $"))
while sales_amount >= 0:
    if sales_amount < 1000:
        bonus_amount = sales_amount * 0.10
    else:
        bonus_amount = sales_amount * 0.15
    print(f"Your bonus is ${bonus_amount:.2f}")
    sales_amount = float(input("Enter value of sales: $"))