import unittest
#from pots_of_gold import LEFT, RIGHT, bestmove

LEFT = 0
RIGHT = -1

def bestmove(pots):
    number_of_pots = len(pots)

    if number_of_pots == 0:
        raise ValueError('No pot')
    elif number_of_pots == 1:
        return pots[LEFT], LEFT
    elif number_of_pots == 2:
        if pots[LEFT] >= pots[RIGHT]:
            return pots[LEFT], LEFT
        else:
            return pots[RIGHT], RIGHT
    else:
        pick_left = pots[LEFT]
        remaining_pots = pots[1:]
        oscore, omove = bestmove(remaining_pots)
        pick_left += sum(remaining_pots) - oscore

        pick_right = pots[RIGHT]
        remaining_pots = pots[:-1]
        oscore, _ = bestmove(remaining_pots)
        pick_right += sum(remaining_pots) - oscore

        if pick_left >= pick_right:
            return pick_left, LEFT
        else:
            return pick_right, RIGHT

class BestMoveTest(unittest.TestCase):
    def test_nopot(self):
        with self.assertRaises(ValueError):
            bestmove([])

    def test_one_pot(self):
        self.assertEqual((3, LEFT), bestmove([3]))

    def test_two_pots(self):
        self.assertEqual((5, LEFT), bestmove([5, 4]))
        self.assertEqual((4, RIGHT), bestmove([2, 4]))

    def test_three_pots(self):
        self.assertEqual((9, LEFT), bestmove([7, 2, 3]))
        self.assertEqual((9, RIGHT), bestmove([3, 2, 7]))
        self.assertEqual((3, LEFT), bestmove([2, 4, 1]))
        self.assertEqual((3, LEFT), bestmove([1, 4, 2]))

    def test_four_pots(self):
        self.assertEqual((7, RIGHT), bestmove([1, 3, 5, 4]))
        self.assertEqual((5, RIGHT), bestmove([1, 4, 2, 1]))

unittest.main(verbosity=1)
