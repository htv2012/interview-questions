#!/usr/bin/env python

import unittest
from largest_sum import largest


class Testlargest(unittest.TestCase):
    def testBentleyCase(self):
        self.assertEqual(187, largest([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]))

    # def testAllNegativesExpectFirstElement(self):
    #     self.assertEqual(-1, largest([-1, -2, -3]))

    # def testAllNegativesExpectMiddleElement(self):
    #     self.assertEqual(-1, largest([-5, -2, -1, -2, -3]))

    # def testAllNegativesExpectLastElement(self):
    #     self.assertEqual(-1, largest([-2, -3, -1]))

    # def testNegativesAndZeroInMiddle(self):
    #     self.assertEqual(0, largest([-1, 0, -2, -3]))

    # def testNegativesAndZeroInFirst(self):
    #     self.assertEqual(0, largest([0, -2, -1, -3]))

    # def testNegativesAndZeroInLast(self):
    #     self.assertEqual(0, largest([-2, -1, -3, 0]))

    # def testAllZero(self):
    #     self.assertEqual(0, largest([0, 0, 0]))

    # def testMixedInput01(self):
    #     self.assertEqual(7, largest([-1, 2, -3, 2, 0, 5, -11]))

    # def testMixedInput02(self):
    #     self.assertEqual(5, largest([-1, -2, 0, 3, -5, 3, 2]))

    # def testMixedInput03(self):
    #     self.assertEqual(6, largest([1, 2, 3]))

    # def testMixedInput04(self):
    #     self.assertEqual(4, largest([4, -1, -2, 2]))

    # def testMixedInput05(self):
    #     self.assertEqual(63, largest([11, 2, 3, -4, 51]))

    # def testMixedInput06(self):
    #     self.assertEqual(2, largest([-1, 2, -3, -4, -5]))

    # def testMixedInput07(self):
    #     self.assertEqual(4, largest([-1, 2, -3, 4, -5]))

    # def testConsecutiveNegatives(self):
    #     self.assertEqual(8, largest([0, 7, -2, -3, 6, -9, -1, -2]))

    # def test1(self):
    #     self.assertEqual(7,  largest([1, -3, 2, 5, -5]))

if __name__ == '__main__':
    unittest.main()
