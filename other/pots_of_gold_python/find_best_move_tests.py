__author__ = 'haiv'

import unittest
import ddt
from pots_of_gold import find_best_move, LEFT, RIGHT


@ddt.ddt
class MyTestCase(unittest.TestCase):
    longMessage = True

    def test_no_pot(self):
        self.assertEqual((0, LEFT), find_best_move([]))

    def test_one_pot(self):
        self.assertEqual((5, LEFT), find_best_move([5]))

    def test_two_pots(self):
        self.assertEqual((5, LEFT), find_best_move([5, 4]))
        self.assertEqual((9, RIGHT), find_best_move([5, 9]))

    @ddt.data(
        ([1, 2, 3], (4, RIGHT)),
        ([2, 3, 1], (3, LEFT))
    )
    def test_three_pots(self, test_data):
        pots, expected = test_data
        self.assertEqual(expected, find_best_move(pots))




if __name__ == '__main__':
    unittest.main()
