"""
https://leetcode.com/problems/multiply-strings/description/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.multiply


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                num1="2",
                num2="3",
                expected="6",
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                num1="123",
                num2="456",
                expected="56088",
            ),
            id="Example 2",
        ),
    ],
)
def test_solution(fut, test_case):
    pass
