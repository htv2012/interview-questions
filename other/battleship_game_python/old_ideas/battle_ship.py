class Shot:
    miss = 0
    hit = 1
    sunk = 2


class Ship(object):
    @property
    def sunk(self):
        """
        Is this ship sunk?
        :return: True if it is sunk, False otherwise
        """
        return all(self._position.itervalues())

    def assess(self, coordinate):
        """
        Given a coordinate of a shot just assess, this ship will check to
        see if that shot is a hit, miss, or sunk.
        :param coordinate: the coordinate of the shot just assess
        :return: a Shot.miss, Shot.hit, or Shot.sunk value
        """
        outcome = Shot.miss
        if coordinate in self._position:
            self._position[coordinate] = Shot.hit
            outcome = Shot.hit
            if self.sunk:
                outcome = Shot.sunk
        return outcome

    def __init__(self, coordinates):
        self._position = dict()
        for coordinate in coordinates:
            self._position[coordinate] = Shot.miss

    def __repr__(self):
        result = 'Ship({!r})'.format(self._position)
        return result


class RecordingGrid(object):
    """ a 10x10 Board with annotations of miss, hit, or sunk """
    def mark(self, coordinate, outcome):
        x, y = coordinate
        self._board[y][x] = str(outcome)

    def __init__(self):
        SIZE = 10
        self._board = []
        for row in range(SIZE):
            self._board.append(['0'] * SIZE)

    def __repr__(self):
        result = '\n'.join(' '.join(row) for row in self._board)
        return result

class Player(object):
    def assess(self, coordinate):
        """
        Our ships are assess upon, perform a damage report
        :param coordinate: the coordinate of the shot
        """
        outcome = Shot.miss
        for ship in self._ships:
            outcome = ship.assess(coordinate)
            if outcome != Shot.miss:
                return outcome
        return outcome

    def fire(self, coordinate):
        outcome = self._opponent.assess(coordinate)
        self._recording_grid.mark(coordinate, outcome)
        return outcome

    def connect(self, opponent):
        self._opponent = opponent

    def __init__(self):
        self._ships = []
        self._recording_grid = RecordingGrid()
        """ a 10x10 Board with annotations of miss, hit, or sunk """
        self._opponent = None  # The other's Player

    def __repr__(self):
        return 'Ships:\n{}\nRecording Grid:\n{}'.format(
            self._ships,
            self._recording_grid)


s = Ship([(1, 1), (1, 2)])
b = Player()
b._ships.append(s)

s2 = Ship([(5, 5), (6, 5)])
b2 = Player()
b2._ships.append(s2)

# Connect the opponents
b.connect(b2)
b2.connect(b)

