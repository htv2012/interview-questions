"""
https://leetcode.com/problems/rings-and-rods/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "rings, expected",
    [
        pytest.param("B0B6G0R6R0R6G9", 1, id="Example 1"),
        pytest.param("B0R0G0R9R0B0G0", 1, id="Example 2"),
        pytest.param("G4", 0, id="Example 3"),
        pytest.param("R0G0B0R1G1B1", 2, id="two rings"),
    ],
)
def test_solution(rings, expected):
    sol = Solution()
    assert sol.countPoints(rings) == expected
