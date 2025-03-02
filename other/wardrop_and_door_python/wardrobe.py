#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import unittest


def wardrobe_and_doorway(a, b, c, x, y):
    """
    Take a wardrobe of dimensions A x B x C and a door way of inner
    dimension X x Y, determine if the wardrobe fits through the
    door way. We assume the width and height of the shortest side
    of the wardrobe must be smaller than those of the door way. For
    example, if the wardrobe is of dimension 5x3x4 then the shortest
    dimension would be 3x4. If the door way's dimension is also
    3x4, we will assume that it will not fit through.

    :param a, b, c: dimensions of the wardrobe
    :param x, y: dimensions of the door way
    :return True if the wardrobe fits through the door way, False
        otherwise
    """
    wwidth, wheight = sorted((a, b, c))[:2]
    dwidth, dheight = sorted((x, y))

    return wwidth < dwidth and wheight < dheight


class WarDrobeTest(unittest.TestCase):
    def test_fit(self):
        self.assertEqual(True, wardrobe_and_doorway(5, 3, 2, 4, 3))

    def test_too_snug(self):
        self.assertEqual(False, wardrobe_and_doorway(5, 3, 4, 4, 3))

    def test_not_fit(self):
        self.assertEqual(False, wardrobe_and_doorway(5, 6, 4, 4, 3))


if __name__ == '__main__':
    unittest.main()
