"""
https://leetcode.com/problems/fibonacci-number/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.fib


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
            n=2,
            expected=1,
        ),
        tc(
            test_id="Example 2",
            n=3,
            expected=2,
        ),
        tc(
            test_id="Example 3",
            n=4,
            expected=3,
        ),
    ],
)
def test_solution(fut, n, expected):
    assert fut(n) == expected
