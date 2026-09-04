"""
https://leetcode.com/problems/finding-3-digit-even-numbers/
"""

import logging

import pytest

from solution import Solution

logger = logging.getLogger("test")


@pytest.mark.parametrize(
    "digits, expected",
    [
        pytest.param(
            [2, 1, 3, 0],
            [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
            id="Example 1",
        ),
        pytest.param(
            [2, 2, 8, 8, 2], [222, 228, 282, 288, 822, 828, 882], id="Example 2"
        ),
        pytest.param([3, 7, 5], [], id="Example 3"),
    ],
)
def test_solution(digits, expected):
    logger.debug(f"{digits = }")
    logger.debug(f"{expected = }")
    sol = Solution()
    assert sol.findEvenNumbers(digits) == expected
