"""
https://leetcode.com/problems/find-the-town-judge/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.findJudge


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["n"],
        kwargs["trust"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "n, trust, expected",
    [
        tc(test_id="Example 1", n=2, trust=[[1, 2]], expected=2),
        tc(test_id="Example 2", n=3, trust=[[1, 3], [2, 3]], expected=3),
        tc(test_id="Example 3", n=3, trust=[[1, 3], [2, 3], [3, 1]], expected=-1),
        tc(test_id="wrong 1", n=3, trust=[[1, 2], [2, 3]], expected=-1),
        tc(test_id="wrong 2", n=1, trust=[], expected=1),
    ],
)
def test_solution(fut, n, trust, expected):
    assert fut(n, trust) == expected
