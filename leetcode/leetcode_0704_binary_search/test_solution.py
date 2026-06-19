"""
https://leetcode.com/problems/binary-search/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.search


def tc(tid: str, **kwargs):
    return pytest.param(types.SimpleNamespace(**kwargs), id=tid)


@pytest.mark.parametrize(
    "test_case",
    [
        tc(
            "Example 1",
            nums=[-1, 0, 3, 5, 9, 12],
            target=9,
            expected=4,
        ),
        tc(
            "Example 2",
            nums=[-1, 0, 3, 5, 9, 12],
            target=2,
            expected=-1,
        ),
        tc("empty array", nums=[], target=1, expected=-1),
        tc("single element, expect found", nums=[9], target=9, expected=0),
        tc("single element, expect not found", nums=[9], target=5, expected=-1),
        tc("large array", nums=list(range(100000)), target=50000, expected=50000),
    ],
)
def test_solution(fut, test_case):
    assert fut(test_case.nums, test_case.target) == test_case.expected
