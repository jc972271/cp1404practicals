"""
CP1404 - Practical 5
Convert colour name to hex code.
"""

NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                "Amber": "#ffbf00", "Amethyst": "#9966cc", "Ash Grey": "#b2beb5"}

colour_name = input("Enter a colour: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter a colour: ").title()