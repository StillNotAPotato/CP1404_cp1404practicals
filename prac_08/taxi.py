"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23 # Class variable, known to all Taxi objects

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel) # pass into parent constructor (inherit name, fuel, odometer)
        self.current_fare_distance = 0
        # total 5 attributes the Taxi has compared to Car's 3 attributes
    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)
    # will also inherit drive(), add_fuel(), __str___(), __init__()
    # __str__() and __init__() are overridden, provide more specialised implementation of your own :O

    def get_fare(self): # new to Taxi only
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):   # new to Taxi only
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):  # overridden method
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven