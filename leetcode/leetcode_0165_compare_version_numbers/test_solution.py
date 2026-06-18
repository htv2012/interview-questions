"""
https://leetcode.com/problems/compare-version-numbers/
"""

import types

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.compareVersion


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                version1="1.2",
                version2="1.10",
                expected=-1,
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                version1="1.01",
                version2="1.001",
                expected=0,
            ),
            id="Example 2",
        ),
        pytest.param(
            types.SimpleNamespace(
                version1="1.0",
                version2="1.0.0.0",
                expected=0,
            ),
            id="Example 3",
        ),
    ],
)
def test_solution(fut, test_case):
    pass
