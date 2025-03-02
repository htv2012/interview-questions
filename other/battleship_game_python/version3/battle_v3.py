#!/usr/bin/env python3
"""
In this implementation, we use 3 pieces of information to keep track of a player's information:

- grid: A dict of coord: ship ID
- status: A dict of coord: hit or sunk
- health: A dict of ship ID: count of cells that are still alive
"""

class Status:
    MISSED = "missed"
    IN_TACT = "in tact"
    HIT = "hit"
    SUNK = "sunk"

class Player:
    def __init__(self):
        self.grid = {}  # A dict of coordinate: ship ID
        self.status = {}  # A dict of coordinate: hit or sunk
        self.health = {}  # A dict of ship ID: count of cells that are still alive

    def __repr__(self):
        return f"Player(grid={self.grid}, status={self.status}, health={self.health})"

    def add_ship(self, ship_id, coordinates):
        for coord in coordinates:
            self.grid[coord] = ship_id
            self.status[coord] = Status.IN_TACT
            self.health.setdefault(ship_id, 0)
            self.health[ship_id] += 1

    def assess(self, coord):
        if coord not in self.grid:
            return Status.MISSED

        if self.status[coord] == Status.IN_TACT:
            ship_id = self.grid[coord]
            self.health[ship_id] -= 1
            self.status[coord] = Status.SUNK if self.health[ship_id] == 0 else Status.HIT
            return self.status[coord]

        return "you are beating a dead horse"

    def fire(self, coord):
        assessment = self.assess(coord)
        print(f"Fire at {coord} ==> {assessment}")


player = Player()
player.add_ship(1, ("A1", "A2", "A3"))

print(f"Player: {player}")

# Misses
player.fire("C3")
player.fire("D5")

# Hit and sunk
player.fire("A3")
player.fire("A1")
player.fire("A2")

# Dead horse
player.fire("A1")
player.fire("A2")
player.fire("A3")

print(f"Player: {player}")