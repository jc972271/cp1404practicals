"""CP1404 - Guitar class."""
class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Formats the output into f string."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self, current_year):
        """Gets the age in years of the guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Verifies if the guitar is vintage (> 50 years old)."""
        return self.get_age(current_year) >= 50