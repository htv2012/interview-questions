# Try out ideas for a battleship board
from __future__ import print_function
# from collections import _repeat


ROWCOUNT = 10
COLCOUNT = 10


class Cell:
    empty = 0
    occupied = 1
    hit = 2


class Assessment:
    missed = 'missed'
    hit = 'hit'
    sink = 'sink'


def show_grid(grid):
    for row in range(ROWCOUNT):
        for col in range(COLCOUNT):
            print(grid[(col, row)], end=' ')
        print()
    print('\n')


def assess(grid, coord, ship_names):
    """
    Given a grid and a coordinate, determine if the shot to
    that coordinate a hit, missed, or sink
    """
    if grid[coord] == Cell.empty:
        return Assessment.missed
    elif grid[coord] == Cell.occupied:
        ship_name = ship_names[coord]
        ship_health[ship_name] -= 1
        grid[coord] = Cell.hit
        if ship_health[ship_name] == 0:
            return Assessment.sink
        return Assessment.hit
    elif grid[coord] == Cell.hit:
        raise ValueError('Fired here already')
    else:
        raise ValueError('Invalid cell')


def fire(x, y):
    # When a shot fired to a coordinate, we know right away if it is a hit or miss
    # by looking up the grid: a Cell.empty means miss
    coord = (x, y)
    print('Shot fired at {} result in a {}'.format(coord, assess(grid, coord, ship_names)))

# grid is a series of coordinates
grid = {(c, r): Cell.empty for r in range(ROWCOUNT) for c in range(COLCOUNT)}

# Ships is a dict where key=coordinate, value=ship name
ship_names = {
    (0, 0): 'a', (0, 1): 'a',
    (1, 2): 'b', (2, 2): 'b', (3, 2): 'b',
}

ship_health = dict()
for ship_name in ship_names.values():
    ship_health.setdefault(ship_name, 0)
    ship_health[ship_name] += 1

# Place the ships on the grid
for coord in ship_names:
    grid[coord] = Cell.occupied

print()
show_grid(grid)

fire(5, 5)
fire(0, 1)
fire(0, 0)
print()
show_grid(grid)
