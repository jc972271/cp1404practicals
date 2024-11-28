"""
CP1404
Band class
"""

class Band:
    """Band class for storing details of a band."""
    def __init__(self, band):
        """Initialise a Band."""
        self.band = band
        self.members = []

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.band} ({[str(member) for member in self.members]})"

    def add(self, member):
        """Add a musician to the band."""
        self.members.append(member)

    def play(self):
        """Return a string showing each band member their first (or no) instrument."""
        string = ""
        for member in self.members:
            string += member.play() + "\n"
        return string