"""
https://leetcode.com/problems/binary-watch/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.readBinaryWatch


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["turnedOn"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "turnedOn, expected",
    [
        tc(
            test_id="Example 1",
            turnedOn=1,
            expected=[
                "0:01",
                "0:02",
                "0:04",
                "0:08",
                "0:16",
                "0:32",
                "1:00",
                "2:00",
                "4:00",
                "8:00",
            ],
        ),
        tc(
            test_id="Example 2",
            turnedOn=9,
            expected=[],
        ),
    ],
)
def test_solution(fut, turnedOn, expected):
    assert fut(turnedOn) == expected
