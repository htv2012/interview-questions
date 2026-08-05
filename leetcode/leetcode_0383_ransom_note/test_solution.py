"""
https://leetcode.com/problems/ransom-note/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.canConstruct


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["ransomNote"],
        kwargs["magazine"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "ransomNote, magazine, expected",
    [
        tc(
            test_id="Example 1",
            ransomNote="a",
            magazine="b",
            expected=False,
        ),
        tc(
            test_id="Example 2",
            ransomNote="aa",
            magazine="ab",
            expected=False,
        ),
        tc(
            test_id="Example 3",
            ransomNote="aa",
            magazine="aab",
            expected=True,
        ),
    ],
)
def test_solution(fut, ransomNote, magazine, expected):
    assert fut(ransomNote, magazine) == expected
