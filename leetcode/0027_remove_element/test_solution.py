#!/usr/bin/env python3
from collections import Counter

import pytest


@pytest.mark.parametrize(
    "nums, val, k, expected",
    [
        pytest.param([3, 2, 2, 3], 3, 2, [2, 2], id="example 1"),
        pytest.param([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3], id="example 2"),
        pytest.param([], 5, 0, [], id="empty list"),
        pytest.param([1, 2, 3, 4, 5], 6, 5, [1, 2, 3, 4, 5], id="no val found"),
        pytest.param([1] * 3, 1, 0, [], id="all val"),
        pytest.param([1], 1, 0, [], id="single-element list, val found"),
        pytest.param([1], 2, 1, [1], id="single-element list, val not found"),
    ],
)
def test_solution(fut, nums, val, k, expected):
    assert fut(nums, val) == k
    actual = Counter(nums[:k])
    expected = Counter(expected)
    assert actual == expected
