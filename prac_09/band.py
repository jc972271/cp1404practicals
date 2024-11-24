"""
CP1404
Band class
"""

class Band:
    """Band class for storing details of a band."""
    def __init__(self, band):
        self.band = band
        self.members = []

    def __str__(self):
        return f"{self.band} ({[str(member) for member in self.members]})"

    def add(self, member):
        self.members.append(member)

    def play(self):
        string = ""
        for member in self.members:
            string += member.play() + "\n"
        return string