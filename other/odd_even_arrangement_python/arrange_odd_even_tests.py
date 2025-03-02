#!/usr/bin/env python
"""
Given a list of integers containing equal number of odd and even
numbers rearrange them in such a way that odd number is at odd
zero-based index.
"""
import unittest
import logging
from arrange_odd_even import arrange_odd_even, isodd

logging.basicConfig(level=logging.INFO, format='%(message)s')


# Since the ddt package is not part of standard library, I don't want to use it
class OddEvenSortTests(unittest.TestCase):
    def test_sorted(self):
        self._do_test([2, 3])
        self._do_test([2, 3, 4, 7])

    def test_not_sorted(self):
        self._do_test([3, 1, 5, 2, 4, 6])
        self._do_test([1, 2, 3, 4])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self._do_test([1, 3, 5, 7, 2, 4, 6])

    def _do_test(self, input_list):
        actual = list(input_list)
        arrange_odd_even(actual)

        logging.info('\nDO TEST: input  = {}'.format(input_list))
        logging.info('DO TEST: output = {}'.format(actual))

        for i, element in enumerate(actual):
            msg = 'Problem at index {}\nInput: {}\nOutput: {}'.format(i, input_list, actual)
            self.assertEqual(0, isodd(i + element), msg)


if __name__ == '__main__':
    unittest.main()
