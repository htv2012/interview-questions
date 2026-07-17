"""
https://leetcode.com/problems/reverse-bits/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.reverseBits


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["n"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "n, expected",
    [
        tc(
            test_id="Example 1",
            n=43261596,
            expected=964176192,
        ),
        tc(
            test_id="Example 2",
            n=2147483644,
            expected=1073741822,
        ),
    ],
)
def test_solution(fut, n, expected):
    assert fut(n) == expected
