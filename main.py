import csv
import math
import random

from player import Player


def read_data(file):
    """
    Read a csv file and store data as a list of Player instances
    :param file: csv file path ('data/chess-players-2.csv')
    :return: players: list of players read from file
    """
    players = []

    with open(file, encoding="utf8", newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            last_name = row['Last name']
            first_name = row['First name']
            full_name = row['Full name']
            countries = row['Countries'].split('-')
            # countries = row['Countries']
            born = row['born']
            died = row['died']

            player = Player(first_name, last_name, full_name, countries, born, died)

            players.append(player)

    print("Total players read from file: " + str(len(players)))
    return players


def print_players(players):
    """
    print all players details
    :param players:
    :return: void
    """
    for player in players:
        player.print_details()


def bubble_sort(players):
    """
    Sorting algorithm of complexity O(n^2)
    :param players: players list
    :return: sorted players list
    """
    n = len(players)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if players[j].__gt__(players[j + 1]):
                players[j], players[j + 1] = players[j + 1], players[j]
                already_sorted = False

        if already_sorted:
            break

    return players


def binary_search(players, other_player):
    """
    Search a sorted array by repeatedly dividing the search interval in half
    :param players: players list read from csv file
    :param other_player: a list of players to see if each one belongs to the players list
    :return: 'm' index on the players list if player is found, -1 if player is not found
    """
    l = 0
    h = len(players) - 1
    c = 0

    while l <= h:
        m = l + (h - l) // 2

        if players[m].__eq__(other_player):
            print('Number of tires: ' + str(c))
            return m

        elif players[m].__lt__(other_player):
            l = m + 1

        else:
            h = m - 1
        c += 1

    print('Number of tires: ' + str(c))
    return -1


if __name__ == '__main__':
    """ Read csv files """
    players = read_data('data/chess-players-2.csv')
    other_players = read_data('data/chess-players-subset.csv')

    """create a list of random chess players from players[] list"""
    random_players = []
    for i in range(0, 100):
        n = random.randint(0, len(players)-1)
        # print(n)
        random_players.append(players[n])

    random_players.append(Player('John', 'Doe', 'John Doe', ['Nowhere'], '?', '?'))

    """ Sort the chess players list """
    bubble_sort(players)

    """ Search for each player in random_players List """
    for op in random_players:

        print('------ Searching: ' + op.first_name + ' ' + op.last_name)
        result = binary_search(players, op)

        if result == -1:
            print("Could not find player")
        else:
            # print(result)
            print("Found Player")
            players[result].print_details()

        print('log(len(players), 2)')
        print (math.log(len(players), 2))
