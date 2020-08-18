class Player:
    def __init__(self, first_name, last_name, full_name, countries, born, died):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.countries = countries
        self.born = born
        self.died = died

    def __lt__(self, other):
        player1 = (self.last_name, self.first_name, self.born)
        player2 = (other.last_name, other.first_name, other.born)

        return player1 < player2

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        player1 = (self.last_name, self.first_name, self.born)
        player2 = (other.last_name, other.first_name, other.born)

        return player1 >= player2

    def __le__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        player1 = (self.last_name, self.first_name, self.born)
        player2 = (other.last_name, other.first_name, other.born)

        return player1 == player2

    def __ne__(self, other):
        return not self.__eq__(other)

    def print_details(self):
        countries_string = ''
        if (len(self.countries) > 1):
            for c in self.countries:
                # print(c)
                countries_string += c + ' , '
        else:
            countries_string = self.countries[0]

        # print("Player details: " + self.first_name + '|' + self.last_name + '|' + countries_string + '|'
        # + self.born + '|' + self.died)
        print(' ---- PLAYER DETAILS ---')
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        print('Countries: ')
        for c in self.countries:
            print('    ' + c)
        print('born: ' + self.born)
        print('death: ' + self.died)
