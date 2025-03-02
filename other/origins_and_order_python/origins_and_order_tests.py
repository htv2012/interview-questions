#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import unittest
from origins_and_order import origins_and_order


class OriginsAndOrderTest(unittest.TestCase):
    def test01(self):
        self.assertEqual('Ambiguous', origins_and_order(3, 30, 3))

    def test02(self):
        self.assertEqual('Ambiguous', origins_and_order(1, 1, 3))

    def test06(self):
        self.assertEqual('Ambiguous', origins_and_order(12, 31, 30))

    def test03(self):
        self.assertEqual('03/19/19', origins_and_order(19, 19, 3))

    def test04(self):
        self.assertEqual('01/01/01', origins_and_order(1, 1, 1))

    def test05(self):
        self.assertEqual('11/13/99', origins_and_order(99, 11, 13))

    def test07(self):
        self.assertEqual('02/28/29', origins_and_order(2, 28, 29))

    def test08(self):
        self.assertEqual('Ambiguous', origins_and_order(2, 12, 12))

    def test_month_with_30_days(self):
        self.assertEqual('04/30/31', origins_and_order(31, 30, 4))

    def test_month_with_31_days(self):
        self.assertEqual('Ambiguous', origins_and_order(31, 30, 5))

    def test_invalid_format(self):
        self.assertIsNone(origins_and_order(32, 32, 32))

if __name__ == '__main__':
    unittest.main()
