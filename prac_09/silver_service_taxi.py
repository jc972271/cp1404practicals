"""
CP1404 Practical
Silver Service Taxi class
"""
from prac_09.car import Car
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with inflated fare costs."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Taxi but with current fare distance."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
