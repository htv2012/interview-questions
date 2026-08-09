"""
https://leetcode.com/problems/insert-interval/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.insert


def tc(id, **kwargs):
    return pytest.param(
        kwargs["intervals"],
        kwargs["newInterval"],
        kwargs["expected"],
        id=id,
    )


@pytest.mark.parametrize(
    "intervals, newInterval, expected",
    [
        tc(
            "Example 1",
            intervals=[[1, 3], [6, 9]],
            newInterval=[2, 5],
            expected=[[1, 5], [6, 9]],
        ),
        tc(
            "Example 2",
            intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            newInterval=[4, 8],
            expected=[[1, 2], [3, 10], [12, 16]],
        ),
        tc("empty list", intervals=[], newInterval=[2, 5], expected=[[2, 5]]),
        tc(
            "insert left, no merge",
            intervals=[[3, 5], [8, 10]],
            newInterval=[1, 2],
            expected=[[1, 2], [3, 5], [8, 10]],
        ),
        tc(
            "insert left, merge",
            intervals=[[1, 3], [6, 9]],
            newInterval=[2, 5],
            expected=[[1, 5], [6, 9]],
        ),
        tc(
            "insert right, no merge",
            intervals=[[1, 3], [6, 9]],
            newInterval=[11, 12],
            expected=[[1, 3], [6, 9], [11, 12]],
        ),
        tc(
            "merge all",
            intervals=[[1, 2], [3, 5], [8, 10]],
            newInterval=[2, 9],
            expected=[[1, 10]],
        ),
        tc(
            "merge all 2",
            intervals=[[1, 3], [6, 9]],
            newInterval=[2, 7],
            expected=[[1, 9]],
        ),
        tc(
            "merge all 3",
            intervals=[[1, 3], [6, 9]],
            newInterval=[3, 6],
            expected=[[1, 9]],
        ),
        tc(
            "merge right",
            intervals=[[1, 3], [6, 9]],
            newInterval=[4, 7],
            expected=[[1, 3], [4, 9]],
        ),
    ],
)
def test_solution(fut, intervals, newInterval, expected):
    #    assert fut(intervals, newInterval) == expected
    pass
