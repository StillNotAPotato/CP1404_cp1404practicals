from car import Car
from random import randint


class UnreliableCar:

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car only if its reliable"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        actual_distance_driven = super().drive(distance)
        return actual_distance_driven
