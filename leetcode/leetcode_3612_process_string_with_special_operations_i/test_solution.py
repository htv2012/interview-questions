"""
https://leetcode.com/problems/process-string-with-special-operations-i/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    """Function under test."""
    sol = Solution()
    return sol.processStr


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                s="a#b%*",
                expected="ba",
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                s="z*#",
                expected="",
            ),
            id="Example 2",
        ),
    ],
)
def test_solution(fut, test_case):
    assert fut(test_case.s) == test_case.expected
