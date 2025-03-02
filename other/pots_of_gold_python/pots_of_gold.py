"""
Pots of Gold Game

http://www.careercup.com/question?id=15422849

Pots of gold game:
Two players A & B. There are pots of gold arranged in
a line, each containing some gold coins (the players can see how many
coins are there in each gold pot - perfect information). They get
alternating turns in which the player can pick a pot from one of the
ends of the line. The winner is the player which has a higher number of
coins at the end. The objective is to "maximize" the number of coins
collected by A, assuming B also plays optimally. A starts the game.

The idea is to find an optimal strategy that makes A win knowing that B
is playing optimally as well. How would you do that?

At the end I was asked to code this strategy!

"""

import cache
import random


LEFT = 0
RIGHT = -1

def generate_pots():
    """
    Generates a number of pots, each pots contain a random number of
    gold coins
    """
    return [random.randint(1, 5) for i in range(6)]


def show_pots(pots):
    """
    Display on the console the pots and its contents
    @param pots A list representing pots of gold coins
    """
    print '\nPots:', pots


@cache.cache
def find_best_move(pots):
    """
    Given a list of pots (list of int), calculate and return a tuple.
    The first value in the tuple is the maximum coins earned, assuming
    that the other player also plays optimally. The second value in the
    tuple is an index indicating which ends of the pots to take: 0 for
    the left end and -1 for the right.
    @param pots The list of pots to pick from
    @return A tuple of (max coins earn, index indicating which end)
    """
    if not pots:
        result = (0, 0)
    elif len(pots) == 1:
        result = (pots[0], 0)
    else:
        total1 = pots[0]
        subtotal1a, dummy = find_best_move(pots[2:])
        subtotal1b, dummy = find_best_move(pots[1:-1])
        total1 += min(subtotal1a, subtotal1b)

        total2 = pots[-1]
        subtotal2a, dummy = find_best_move(pots[1:-1])
        subtotal2b, dummy = find_best_move(pots[:-2])
        total2 += min(subtotal2a, subtotal2b)

        choice = 0 if total1 > total2 else -1
        result = (max(total1, total2), choice)

    return result

class Player(object):
    """
    Simulates a player: human or robot.
    """

    def __init__(self):
        """
        Constructor which reset the score (number of coins) for each
        player.
        """
        self.total = 0  # The total coins this player collected so far
        self.name = 'Unknown'

    def __str__(self):
        return self.name

    def report_score(self):
        report = '{} has {} coin'.format(self.name, self.total)
        if self.total > 1:
            report += 's'
        return report

class Robot(Player):
    """
    Simulate a robot player. The robot will try its best to win the
    game.
    """

    def __init__(self, robot_name='Johnny Five'):
        super(Robot, self).__init__()
        self.name = robot_name
        print 'Hello, I am {}. I will be your opponent.'.format(robot_name)

    def play(self, pots):
        """
        Simulate a robot making decision of which move to play.
        """
        show_pots(pots)
        _, choice = find_best_move(pots)
        points = pots.pop(choice)
        self.total += points
        print 'I pick: {}, total: {}'.format(points, self.total)

class Human(Player):
    """
    This is a human player: the human will key in his or her choices,
    effectively playing against the robot (computer).
    """

    def __init__(self, human_name='Human'):
        super(Human, self).__init__()
        self.name = human_name

    def play(self, pots):
        """
        Asks the human player (via the console) to make a move by
        selecting a pot from the left or right
        """
        show_pots(pots)
        while True:
            if len(pots) == 1:
                choice = 'L'
            else:
                choice = raw_input("{}'s choice (L/R): ".format(self.name)).upper()
            if choice == 'L':
                points = pots.pop(0)
                break
            elif choice == 'R':
                points = pots.pop()
                break
        self.total += points
        print '{} picked: {}, total: {}'.format(self.name, points, self.total)

def main():
    """
    Starts a Pots-of-Gold game, pitching the human vs. robot player
    """
    robot = Robot()
    human = Human(raw_input('What is your name? '))
    players = [human, robot]

    pots = generate_pots()
    show_pots(pots)

    while True:
        human_first = raw_input('Do you want to go first? ').upper()
        if human_first == 'Y':
            turn = 0
            break
        elif human_first == 'N':
            turn = 1
            break

    while pots:
        players[turn].play(pots)
        turn = 1 - turn

    print '\nGame End.'
    # print '{} has {} coin(s)'.format(human.name, human.total)
    # print '{} has {} coin(s)'.format(robot.name, robot.total)
    print human.report_score()
    print robot.report_score()
    if human.total > robot.total:
        print '{} won'.format(human.name)
    elif human.total < robot.total:
        print '{} won'.format(robot)
    else:
        print 'Tie'


if __name__ == '__main__':
    main()
