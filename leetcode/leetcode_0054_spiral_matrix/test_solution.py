"""
https://leetcode.com/problems/spiral-matrix/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.spiralOrder


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                expected=[1, 2, 3, 6, 9, 8, 7, 4, 5],
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                expected=[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            ),
            id="Example 2",
        ),
    ],
)
def test_solution(fut, test_case):
    assert fut(test_case.matrix) == test_case.expected
