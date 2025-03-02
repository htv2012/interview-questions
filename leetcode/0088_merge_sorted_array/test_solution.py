#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        pytest.param(
            [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6], id="example 1"
        ),
        pytest.param([1], 1, [], 0, [1], id="example 2"),
        pytest.param([0], 0, [1], 1, [1], id="example3"),
        pytest.param([1, 3, 5, 0, 0], 3, [2, 6], 2, [1, 2, 3, 5, 6], id="custom1"),
    ],
)
def test_solution(fut, nums1, m, nums2, n, expected):
    fut(nums1, m, nums2, n)
    assert nums1 == expected
