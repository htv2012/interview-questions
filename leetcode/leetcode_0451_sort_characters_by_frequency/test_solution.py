"""
https://leetcode.com/problems/sort-characters-by-frequency/
"""

import itertools

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.frequencySort


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["s"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "s, expected",
    [
        tc(test_id="Example 1", s="tree", expected="eetr"),
        tc(test_id="Example 2", s="cccaaa", expected="cccaaa"),
        tc(test_id="Example 3", s="Aabb", expected="bbaA"),
        tc(test_id="empty array", s="", expected=""),
        tc(test_id="large", s="a" * 5 * 10**5, expected="a" * 5 * 10**5),
    ],
)
def test_solution(fut, s, expected):
    actual = fut(s)
    last_count = None
    for _, group in itertools.groupby(actual):
        freq = len(list(group))
        if last_count is not None:
            assert last_count >= freq
        last_count == freq
