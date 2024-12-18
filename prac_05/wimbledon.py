"""
CP1404 - Practical 5
Wimbledon data-reading, processing and displaying
"""

import csv

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_PLAYER = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    player_to_wins, countries = format_records(records)
    display_results(player_to_wins, countries)

def display_results(player_to_wins, countries):
    """Displays the wimbledon champions the countries the winners played for."""
    print("Wimbledon Champions:")
    for player in player_to_wins:
        print(f"{player} {player_to_wins[player]}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def format_records(records):
    """Converts a list of records into a format that can be more easily used."""
    player_to_wins = {}
    countries = set([country[INDEX_COUNTRY] for country in records])
    for record in records:
        if record[INDEX_PLAYER] in player_to_wins:
            player_to_wins[record[INDEX_PLAYER]] += 1
        else:
            player_to_wins[record[INDEX_PLAYER]] = 1
    return player_to_wins, countries

def get_records(filename):
    """Opens a CSV file and returns a list of records."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        return list(csv.reader(in_file))


main()
