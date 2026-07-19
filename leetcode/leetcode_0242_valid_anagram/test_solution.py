"""
https://leetcode.com/problems/valid-anagram/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.isAnagram


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["s"],
        kwargs["t"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "s, t, expected",
    [
        tc(
            test_id="Example 1",
            s="anagram",
            t="nagaram",
            expected=True,
        ),
        tc(
            test_id="Example 2",
            s="rat",
            t="car",
            expected=False,
        ),
        tc(
            test_id="wrong1",
            s="aacc",
            t="ccac",
            expected=False,
        ),
    ],
)
def test_solution(fut, s, t, expected):
    assert fut(s, t) == expected
