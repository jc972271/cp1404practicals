"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from random import randint

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes a reliability."""
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but check whether the car starts."""
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
