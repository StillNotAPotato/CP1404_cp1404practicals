import datetime

VINTAGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar object details"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        today = datetime.today()
        guitar_age = today.year - self.year
        return guitar_age

    def is_vintage(self):
        pass
