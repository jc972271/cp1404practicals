"""
CP1404 - Practical - Extension
Code for estimating an electricity bill
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")

tariff = int(input("Which tariff? 11 or 31: "))
while tariff != 11 and tariff != 31:
    print("Please enter 11 or 31")
    tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    price_per_kwh = TARIFF_11
elif tariff == 31:
    price_per_kwh = TARIFF_31

daily_kwh = float(input("Enter daily use in kWh: "))
billing_days = float(input("Enter number of billing days: "))

estimated_bill = (price_per_kwh * daily_kwh * billing_days)

print(f"Estimated bill: ${estimated_bill:.2f}")