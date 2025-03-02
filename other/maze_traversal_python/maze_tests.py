#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import logging
import unittest

from maze import Cell, find_path


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class MazeTests(unittest.TestCase):
    def test_start_is_dest(self):
        start = Cell()
        dest = Cell()
        self.assertEqual([start], find_path(start, start))


if __name__ == '__main__':
    unittest.main()
