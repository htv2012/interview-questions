#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import logging
import operator
import unittest
import ddt


logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def product(seq):
    """
    Given an array of integers, return another array of the same
    size, such that each member is equal to the product of all other
    members in the array, except for the one in that position
    """
    logging.debug('seq: {}'.format(seq))
    prod = reduce(operator.mul, seq, 1)
    logging.debug('prod: {}'.format(prod))
    result = [prod / element if element else prod for element in seq]
    return result


@ddt.ddt
class ProdTest(unittest.TestCase):

    test_data = {
        'case 1': ([2, 3, 4], [12, 8, 6]),
        'case 2': ([1, 2, 3], [6, 3, 2]),
        'zero': ([2, 0, 3], [3, 6, 2]),
    }

    @ddt.data(*test_data)
    def test1(self, tc):
        test_input, expected = self.test_data[tc]
        actual = product(test_input)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
