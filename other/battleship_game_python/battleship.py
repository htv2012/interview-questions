#!/usr/bin/env python
# Idea: instead of a grid, we only store information about ships
# Ships is a dictionary where key=coordinate, and value = ship ID plus
# hit/miss information

from __future__ import print_function


# Make `input` works in both Python 2.x and 3.x
try:
    input = raw_input
except NameError:
    pass


class Assessment:
    not_fired = '.'
    missed = '-'
    hit = 'x'
    sunk = 'X'
    hit_again = 'fired here before'


class Player(object):
    def __init__(self, name):
        self.name = name
        self.ships = dict()
        self.health = dict()
        self.next_id = 2
        self.rows = range(1, 11)
        self.columns = 'ABCDEFGHIJ'
        self._tracking_grid = dict()
        for row in self.rows:
            for column in self.columns:
                coord = '{}{}'.format(column, row)
                self._tracking_grid[coord] = Assessment.not_fired

    def play_with(self, other):
        self.opponent = other

    def add_ship(self, *coords):
        self.ships.update(dict.fromkeys(coords, self.next_id))
        self.health[self.next_id] = len(coords)
        self.next_id <<= 1

    def assess(self, coord):
        try:
            if self._is_hit(coord):
                return Assessment.hit_again

            self._mark_as_hit(coord)
            if self._is_sunk(coord):
                return Assessment.sunk
            return Assessment.hit
        except KeyError:
            return Assessment.missed

    def shoot(self):
        coord = input('Coordinate: ').upper()
        result = self.opponent.assess(coord)
        if result != Assessment.hit_again:
            self._tracking_grid[coord] = result
        self.show()

    def show(self):
        print()
        print("{}'s board".format(self.name))
        for row in zip(self.iter_my_grid, self.iter_tracking_grid):
            print('    '.join(row))
        print()

    @property
    def iter_my_grid(self):
        yield 'MY SHIPS                          '
        yield '   |  ' + '  '.join(self.columns)
        yield '----------------------------------'
        for row in self.rows:
            text = '{:>2} |'.format(row)
            for column in self.columns:
                coord = '{}{}'.format(column, row)
                text += '{:>3}'.format(self.ships.get(coord, '.'))
            yield text

    @property
    def iter_tracking_grid(self):
        yield 'ENERMY SHIPS                      '
        yield '   |  ' + '  '.join(self.columns)
        yield '----------------------------------'
        for row in self.rows:
            text = '{:>2} |'.format(row)
            for column in self.columns:
                coord = '{}{}'.format(column, row)
                text += '{:>3}'.format(self._tracking_grid[coord])
            yield text

    def _is_hit(self, coord):
        return self.ships[coord] & 1

    def _is_sunk(self, coord):
        ship_id = self._get_ship_id(coord)
        return self.health[ship_id] == 0

    def _mark_as_hit(self, coord):
        ship_id = self._get_ship_id(coord)
        self.ships[coord] |= 1
        self.health[ship_id] -= 1

    def _get_ship_id(self, coord):
        ship_id = (self.ships[coord] >> 1) << 1
        return ship_id


if __name__ == '__main__':
    player1 = Player('COMPUTER')
    player2 = Player('Hai')
    player2.play_with(player1)

    player1.add_ship('A1', 'B1')
    player1.add_ship('D1', 'D2', 'D3')
    player1.add_ship('C5', 'C6', 'C7')
    player1.add_ship('G3', 'G4', 'G5', 'G6')
    player1.add_ship('C9', 'D9', 'E9', 'F9', 'G9')

    shots_count = 5
    print('You are to fire {} shots'.format(shots_count))
    for _ in range(shots_count):
        player2.shoot()
    print('-' * 80)
    player1.show()
