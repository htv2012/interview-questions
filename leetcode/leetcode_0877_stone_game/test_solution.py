"""
https://leetcode.com/problems/stone-game/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "piles, expected",
    [
        pytest.param([5, 3, 4, 5], True, id="Example 1"),
        pytest.param([3, 7, 2, 3], True, id="Example 2"),
        pytest.param(
            [
                7,
                7,
                12,
                16,
                41,
                48,
                41,
                48,
                11,
                9,
                34,
                2,
                44,
                30,
                27,
                12,
                11,
                39,
                31,
                8,
                23,
                11,
                47,
                25,
                15,
                23,
                4,
                17,
                11,
                50,
                16,
                50,
                38,
                34,
                48,
                27,
                16,
                24,
                22,
                48,
                50,
                10,
                26,
                27,
                9,
                43,
                13,
                42,
                46,
                24,
            ],
            True,
            id="timeout",
        ),
    ],
)
def test_solution(piles, expected):
    sol = Solution()
    assert sol.stoneGame(piles) == expected
