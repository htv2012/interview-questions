"""
https://leetcode.com/problems/word-pattern/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.wordPattern


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["pattern"],
        kwargs["s"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        tc(
            test_id="Example 1",
            pattern="abba",
            s="dog cat cat dog",
            expected=True,
        ),
        tc(
            test_id="Example 2",
            pattern="abba",
            s="dog cat cat fish",
            expected=False,
        ),
        tc(
            test_id="Example 3",
            pattern="aaaa",
            s="dog cat cat dog",
            expected=False,
        ),
        tc(test_id="wrong 1", pattern="abba", s="dog dog dog dog", expected=False),
    ],
)
def test_solution(fut, pattern, s, expected):
    assert fut(pattern, s) is expected
