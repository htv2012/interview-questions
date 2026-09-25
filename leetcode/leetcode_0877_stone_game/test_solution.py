"""
https://leetcode.com/problems/stone-game/
"""

import json

import pytest

from solution import Solution


def param(filename):
    with open(filename) as stream:
        t = json.load(stream)
    return pytest.param(t["piles"], t["expected"], id=t["id"])


@pytest.mark.parametrize(
    "piles, expected",
    [
        pytest.param([5, 3, 4, 5], True, id="Example 1"),
        pytest.param([3, 7, 2, 3], True, id="Example 2"),
        param("timeout1.json"),
        param("timeout2.json"),
    ],
)
def test_solution(piles, expected):
    sol = Solution()
    assert sol.stoneGame(piles) == expected
