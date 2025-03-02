import pytest


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([3, 2, 3], 3, id="example 1"),
        pytest.param([2, 2, 1, 1, 1, 2, 2], 2, id="example 2"),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected
