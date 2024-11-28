"""CP1404 - Testing silver service taxi class."""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

distance = 18
fanciness = 2

my_taxi = SilverServiceTaxi("Hummer", 100, fanciness)

my_taxi.drive(distance)
expected_price = (distance * fanciness * Taxi.price_per_km) + SilverServiceTaxi.flagfall
print(expected_price)
#assert my_taxi.get_fare() == expected_price

print(my_taxi)
print(f"Price of trip is ${my_taxi.get_fare():.2f}")
