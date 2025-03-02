#!/usr/bin/env python3
import pytest

from three_sum import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.threeSum


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]], id="example 1"),
        pytest.param([0, 1, 1], [], id="example 2"),
        pytest.param([0, 0, 0], [[0, 0, 0]], id="example 3"),
        pytest.param([1, -1], [], id="not enough"),
    ],
)
def test_solution(fut, indata, expected):
    actual = fut(indata)
    for triplet in actual:
        expected.remove(triplet)
    assert expected == []
