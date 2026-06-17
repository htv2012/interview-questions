"""
https://leetcode.com/problems/search-insert-position/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.searchInsert


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                nums=[1, 3, 5, 6],
                target=5,
                expected=2,
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                nums=[1, 3, 5, 6],
                target=2,
                expected=1,
            ),
            id="Example 2",
        ),
        pytest.param(
            types.SimpleNamespace(
                nums=[1, 3, 5, 6],
                target=7,
                expected=4,
            ),
            id="Example 3",
        ),
        pytest.param(
            types.SimpleNamespace(
                nums=[1, 3, 5, 6],
                target=0,
                expected=0,
            ),
            id="wrong answer",
        ),
        pytest.param(
            types.SimpleNamespace(
                nums=[],
                target=10,
                expected=0,
            ),
            id="empty array",
        ),
    ],
)
def test_solution(fut, test_case):
    assert fut(test_case.nums, test_case.target) == test_case.expected
