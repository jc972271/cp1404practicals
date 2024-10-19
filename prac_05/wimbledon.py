"""
CP1404 - Practical 5
Wimbledon data-reading, processing and displaying
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    wimbledon_records = open_file(FILENAME)
    player_to_wins = get_player_to_wins(wimbledon_records)
    print_wimbledon_champions(player_to_wins)

    print()
    print("These 12 countries have won Wimbledon:")
    print(", ".join(sorted(set([country[1] for country in wimbledon_records]))))


def print_wimbledon_champions(player_to_wins):
    print("Wimbledon Champions:")
    for player in player_to_wins:
        print(f"{player} {player_to_wins[player]}")


def get_player_to_wins(wimbledon):
    player_to_wins = {}
    for line in wimbledon:
        if line[2] in player_to_wins:
            player_to_wins[line[2]] += 1
        else:
            player_to_wins[line[2]] = 1
    return player_to_wins


def open_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        return list(csv.reader(in_file))


main()
