""" A bare bone battleship to desmonstrate the design """
from __future__ import print_function


class Player(object):
    def __init__(self):
        # ships is a dictionary where as the keys are the coordinates of the
        # occupying ships and the values hold the ship ID plus hit information.
        # For example, if the value is 3 then it means ship ID 3 occupies this
        # coordinate; a value of 103 means the same, except the ship was hit at
        # this coordinate. A complete example, {'A1': 3, 'A2': 3, 'A3': 103}
        # means the ship ID 3 occupies coordinates A1, A2, and A3; it was hit
        # at coordinate A3
        self.ships = dict()

        # health is a dictionary indicating the health of a ship. The keys are
        # the ship IDs and the values hold the count of coordinates that are
        # still in tact (not hit). When a value gets to zero, the ship is sunk
        self.health = dict()

    def assess(self, coord):
        HIT_MARKER = 100
        if coord not in self.ships:
            return 'missed'

        if self.ships[coord] > HIT_MARKER:
            return 'dead horse'

        ship_number = self.ships[coord]
        self.ships[coord] += HIT_MARKER
        self.health[ship_number] -= 1

        if self.health[ship_number] == 0:
            return 'sunk'
        return 'hit'


if __name__ == '__main__':
    player1 = Player()

    # Ship ID 2, at coordinates C3, D3, and E3
    player1.ships.update(dict(C3=2, D3=2, E3=2))
    player1.health[2] = 3

    coord = 'A2'; print(coord, '==>', player1.assess(coord))  # Missed
    coord = 'A1'; print(coord, '==>', player1.assess(coord))

    coord = 'C3'; print(coord, '==>', player1.assess(coord))  # Hit ship 2
    coord = 'E3'; print(coord, '==>', player1.assess(coord))  # Hit ship 2
    coord = 'D3'; print(coord, '==>', player1.assess(coord))  # Sunk ship 2

    coord = 'C3'; print(coord, '==>', player1.assess(coord))  # Dead horse
