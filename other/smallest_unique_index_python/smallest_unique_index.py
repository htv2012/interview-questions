#!/usr/bin/env python
"""
Problem: Given a list of integer, return the index of the smallest
unique number.

Example:
[5, 2, 5, 4, 2, 7]  # 4 is the smallest unique number, index = 3
"""


import unittest
from collections import Sequence

COUNT = 0
INDEX = 1


def smallest_unique_index(lst):
    if not isinstance(lst, Sequence):
        raise ValueError('Not a squence')
    if not lst:
        raise ValueError('Empty list')
    counter = {}  # {item: [count, index]}
    for index, item in enumerate(lst):
        counter.setdefault(item, [0, index])[COUNT] += 1

    unique = (k for k, (count, index) in counter.items() if count == 1)
    smallest = min(unique)
    return counter[smallest][INDEX]


class SmallestUniqueIndexTest(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_unique_index([])

    def test_not_a_list(self):
        with self.assertRaises(ValueError):
            smallest_unique_index(15)
        with self.assertRaises(ValueError):
            smallest_unique_index(dict())

    def test_normal(self):
        self.assertEqual(
            5,
            smallest_unique_index([5, 2, 3, 2, 3, 4, 7]))


if __name__ == '__main__':
    unittest.main()
