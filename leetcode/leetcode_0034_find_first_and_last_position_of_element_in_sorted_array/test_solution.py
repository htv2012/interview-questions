import pytest


@pytest.mark.parametrize(
    ["nums", "target", "expected"],
    [
        pytest.param([5, 7, 7, 8, 8, 10], 8, [3, 4], id="Example 1"),
        pytest.param([5, 7, 7, 8, 8, 10], 6, [-1, -1], id="Example 2"),
        pytest.param([], 0, [-1, -1], id="Example 3"),
        pytest.param([1, 2, 3, 3, 3, 3, 4, 5, 9], 3, [2, 5], id="wrong 1"),
        pytest.param([1], 1, [0, 0], id="wrong 2"),
        pytest.param([5, 5, 5], 5, [0, 2], id="found both ends"),
        pytest.param([1, 2, 3, 4], 5, [-1, -1], id="too big"),
        pytest.param([1, 2, 3, 4], 0, [-1, -1], id="too small"),
    ],
)
def test_solution(fut, nums, target, expected):
    assert fut(nums, target) == expected
