import csv
import math
import random
import sort
import search

from player import Player


def read_data(file):
    """
    Read a csv file and store data as a list of Player instances
    :param file: csv file path ('data/chess-players-2.csv')
    :return: players: list of players read from file
    """
    players = []

    with open(file, mode='r', encoding="utf8", newline='') as csv_file:
        # reader = csv.DictReader(csv_file)
        reader = csv.DictReader(csv_file, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            last_name = row['Last name']
            first_name = row['First name']
            full_name = row['Full name']
            countries = row['Countries'].split(',')
            # countries = row['Countries']
            born = row['born']
            died = row['died']
            player = Player(first_name, last_name, full_name, countries, born, died)
            players.append(player)

    print("Total players read from file: " + str(len(players)))
    return players


if __name__ == '__main__':
    """ Read csv files """
    players = read_data('data/chess-players.csv')
    print(len(players))
    other_players = read_data('data/chess-players-2-subset.csv')

    """create a list of random chess players from players[] list"""
    random_players = []
    n = int(input("Enter number of random selected players from the list to search: "))

    for i in range(0, n):
        index = random.randint(0, len(players)-1)
        random_players.append(players[index])

    random_players.append(Player('John', 'Doe', 'John Doe', ['Nowhere'], '?', '?'))

    """ Sort the chess players list """
    sort.insertion_sort(players)

    """ Search for each player in random_players List """
    for op in random_players:

        print('------ Searching: ' + op.first_name + ' ' + op.last_name)

        result = search.binary_search(players, op)

        if result == -1:
            print("Could not find player")
        else:
            print("Found Player")
            players[result].print_details()

        # print('log(len(players), 2)')
        # print (math.log(len(players), 2))
