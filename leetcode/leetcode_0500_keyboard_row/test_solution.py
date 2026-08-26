"""
https://leetcode.com/problems/keyboard-row/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.findWords


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["words"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "words, expected",
    [
        tc(
            test_id="Example 1",
            words=["Hello", "Alaska", "Dad", "Peace"],
            expected=["Alaska", "Dad"],
        ),
        tc(
            test_id="Example 2",
            words=["omk"],
            expected=[],
        ),
        tc(
            test_id="Example 3",
            words=["adsdf", "sfd"],
            expected=["adsdf", "sfd"],
        ),
    ],
)
def test_solution(fut, words, expected):
    assert fut(words) == expected
