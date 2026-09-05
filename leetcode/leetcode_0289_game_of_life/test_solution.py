"""
https://leetcode.com/problems/game-of-life/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "board, expected",
    [
        pytest.param(
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
            id="Example 1",
        ),
        pytest.param([[1, 1], [1, 0]], [[1, 1], [1, 1]], id="Example 2"),
    ],
)
def test_solution(board, expected):
    sol = Solution()
    sol.gameOfLife(board)
    assert board == expected
