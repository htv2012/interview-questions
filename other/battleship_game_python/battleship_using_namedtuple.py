#!/usr/bin/env python
from __future__ import print_function
from collections import namedtuple

Player = namedtuple('Player', 'ships health')


def assess(player, coordinate):
    """
    Given a player and a coordinate that the enermy fired at this player, return
    one of: 'missed', 'hit', 'sunk', or 'dead horse' (meaning it was a hit
    before, there is not point hitting this spot again).

    :param player: A Player object
    :param coordinate: The coordinate the enermy fired at
    """
    HIT_MARKER = 10

    if coordinate not in player.ships:
        return 'missed'

    if player.ships[coordinate] > HIT_MARKER:
        return 'dead horse'

    ship_id = player.ships[coordinate]
    player.ships[coordinate] += HIT_MARKER
    player.health[ship_id] -= 1

    if player.health[ship_id] == 0:
        return 'sunk'

    return 'hit'

if __name__ == '__main__':
    player1 = Player(dict(), dict())
    player1.ships.update(dict(A1=1, A2=1))  # Ship with ID 1
    player1.health[1] = 2

    coordinate = 'A5'
    print(coordinate, '==>', assess(player1, coordinate))
    coordinate = 'A1'
    print(coordinate, '==>', assess(player1, coordinate))
    coordinate = 'A2'
    print(coordinate, '==>', assess(player1, coordinate))
    coordinate = 'A2'
    print(coordinate, '==>', assess(player1, coordinate))
