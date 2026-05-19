"""
https://leetcode.com/problems/diameter-of-binary-tree/
"""

import pytest


@pytest.mark.parametrize(
    ["root", "expected"],
    [
        pytest.param([1, 2, 3, 4, 5], 3, id="Example 1"),
        pytest.param([1, 2], 1, id="Example 2"),
    ],
)
def test_solution(fut, root, expected):
    assert fut(root) == expected
