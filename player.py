class Player:
    def __init__(self, first_name, last_name, full_name, countries, born, died):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.countries = countries
        self.born = born
        self.died = died

    def __lt__(self, other):
        player = (self.last_name, self.first_name, self.born)
        other_player = (other.last_name, other.first_name, other.born)

        return player < other_player

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        player = (self.last_name, self.first_name, self.born)
        other_player = (other.last_name, other.first_name, other.born)

        return player >= other_player

    def __le__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        player = (self.last_name, self.first_name, self.born)
        other_player = (other.last_name, other.first_name, other.born)

        return player == other_player

    def __ne__(self, other):
        return not self.__eq__(other)

    def print_details(self):
        print(' ---- PLAYER DETAILS ---')
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        print('Countries: ')
        for c in self.countries:
            print('    ' + c)
        print('born: ' + self.born)
        print('death: ' + self.died)
