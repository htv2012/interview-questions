"""
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "operations, expected",
    [
        pytest.param(["--X", "X++", "X++"], 1, id="Example 1"),
        pytest.param(["++X", "++X", "X++"], 3, id="Example 2"),
        pytest.param(["X++", "++X", "--X", "X--"], 0, id="Example 3"),
    ],
)
def test_solution(operations, expected):
    sol = Solution()
    assert sol.finalValueAfterOperations(operations) == expected
