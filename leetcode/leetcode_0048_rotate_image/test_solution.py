"""
https://leetcode.com/problems/rotate-image/description/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.rotate


def mprint(mat):
    for row in mat:
        print(" ".join(f"{c:>2}" for c in row))


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                expected=[[7, 4, 1], [8, 5, 2], [9, 6, 3]],
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
                expected=[
                    [15, 13, 2, 5],
                    [14, 3, 4, 1],
                    [12, 6, 8, 9],
                    [16, 7, 10, 11],
                ],
            ),
            id="Example 2",
        ),
    ],
)
def test_solution(fut, test_case):
    print("Original:")
    mprint(test_case.matrix)
    fut(test_case.matrix)
    print("Rotated:")
    mprint(test_case.matrix)
    assert test_case.matrix == test_case.expected
