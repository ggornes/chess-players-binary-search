import csv
from player import Player



def read_data():
    players = []

    with open('data/chess-players-2.csv', encoding="utf8", newline='') as csv_file:
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
    for player in players:
        player.print_details()


def bubble_sort(players):
    n = len(players)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if players[j].__gt__(players[j + 1]):
                players[j], players[j+1] = players[j+1], players[j]
                already_sorted = False

        if already_sorted:
            break

    return players


if __name__ == '__main__':
    players = read_data()
    # print_players(players)

    bubble_sort(players)

    print_players(players)




