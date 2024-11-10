"""Project Class"""
class Project:
    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        """Checks if completion = 100%."""
        return self.completion == 100

    def date_filter(self, date):
        """Checks if the start date is greater than or equal to a date."""
        return self.start_date >= date
