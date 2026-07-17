"""
https://leetcode.com/problems/happy-number/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.isHappy


@pytest.mark.parametrize("n", [19, 7])
def test_expected_true(fut, n):
    assert fut(n) is True


@pytest.mark.parametrize("n", [2, 3, 4, 2147483648])
def test_expected_false(fut, n):
    assert fut(n) is False
