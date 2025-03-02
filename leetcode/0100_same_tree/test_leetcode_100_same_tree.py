#!/usr/bin/env python3
import pytest
from tree import breadth_first_build

from leetcode_100_same_tree import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.isSameTree


@pytest.mark.parametrize(
    "p, q,expected",
    [
        pytest.param([1, 2, 3], [1, 2, 3], True, id="example 1"),
        pytest.param([1, 2], [1, None, 2], False, id="example 2"),
        pytest.param([1, 2, 1], [1, 1, 2], False, id="example 3"),
    ],
)
def test_solution(fut, p, q, expected):
    p = breadth_first_build(p)
    q = breadth_first_build(q)
    assert fut(p, q) is expected
