"""
https://leetcode.com/problems/reverse-string-ii/
"""

import pytest

from solution import Solution


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["s"],
        kwargs["k"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "s, k, expected",
    [
        tc(
            test_id="Example 1",
            s="abcdefg",
            k=2,
            expected="bacdfeg",
        ),
        tc(
            test_id="Example 2",
            s="abcd",
            k=2,
            expected="bacd",
        ),
    ],
)
def test_solution(s, k, expected):
    sol = Solution()
    assert sol.reverseStr(s, k) == expected
