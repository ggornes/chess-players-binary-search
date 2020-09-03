import unittest
from player import Player
from sort import bubble_sort
from search import binary_search
from sort import insertion_sort

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.players = []
        self.player1 = Player('John', 'Doe', 'John Doe', ['Nowhere'], '?', '?')
        self.player2 = Player('Alex', 'Doe', 'Alex Doe', ['Nowhere'], '?', '?')
        self.player3 = Player('Barry', 'Doe', 'Barry Doe', ['Nowhere'], '?', '?')
        self.players.append(self.player1)
        self.players.append(self.player2)


    def test_search_player_not_found(self):
        result = binary_search(self.players, self.player3)
        self.assertEqual(result, -1)

    def test_search_player_found(self):
        result = binary_search(self.players, self.player1)
        self.assertEqual(result, 0)

    def test_insertion_sort(self):
        expected_sorted_list = [self.player2, self.player1]
        sorted_players = insertion_sort(self.players)

        for i in range(0,2):
            self.assertEqual(sorted_players[i], expected_sorted_list[i])
