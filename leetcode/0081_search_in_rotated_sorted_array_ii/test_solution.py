#!/usr/bin/env python3
import pytest

target = 2
[1, 5, 6, 0, 0, 1]


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        pytest.param([2, 5, 6, 0, 0, 1, 2], 0, True, id="example 1"),
        pytest.param([2, 5, 6, 0, 0, 1, 2], 3, False, id="example 2"),
        pytest.param([], 1, False, id="empty list"),
        pytest.param([1], 2, False, id="single-element list, expected false"),
        pytest.param([1], 1, True, id="single-element list, expected true"),
        pytest.param([2, 2, 5, 6, 0, 0, 1, 2], 5, True, id="forward with dup"),
        pytest.param([2, 2, 5, 6, 0, 0, 1, 2], 6, True, id="forward with dup2"),
    ],
)
def test_solution(fut, nums, target, expected):
    assert fut(nums, target) == expected
