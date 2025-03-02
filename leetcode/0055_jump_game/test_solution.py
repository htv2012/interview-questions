#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([2, 3, 1, 1, 4], True, id="example 1"),
        pytest.param([3, 2, 1, 0, 4], False, id="example 2"),
        pytest.param([3, 2, 1, 0, 0], False, id="my 1"),
        pytest.param(
            list(range(10000, -1, -1)) + [0],
            False,
            id="wrong 1",
        ),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected
