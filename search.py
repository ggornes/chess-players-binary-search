def binary_search(array, element):
    """
    Search a sorted array by repeatedly dividing the search interval in half
    :param players: players list read from csv file
    :param other_player: a list of players to see if each one belongs to the players list
    :return: 'm' index on the players list if player is found, -1 if player is not found
    """
    l = 0
    h = len(array) - 1
    c = 0

    while l <= h:
        m = l + (h - l) // 2

        if array[m] == element:
            print('Number of tries: ' + str(c))
            return m

        elif array[m] < element:
            l = m + 1

        else:
            h = m - 1
        c += 1

    print('Number of tries: ' + str(c))
    return -1