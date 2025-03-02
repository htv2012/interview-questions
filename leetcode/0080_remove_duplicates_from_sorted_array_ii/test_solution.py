#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "nums, expected_count, expected_array",
    [
        pytest.param([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3], id="example 1"),
        pytest.param(
            [0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3], id="example 2"
        ),
        pytest.param([1] * 30000, 2, [1, 1], id="my 1"),
    ],
)
def test_solution(fut, nums, expected_count, expected_array):
    assert fut(nums) == expected_count
    assert nums[:expected_count] == expected_array


@pytest.mark.slow
def test_all_unique_values(fut):
    expected = 10**8
    nums = list(range(expected))
    assert fut(nums) == expected
