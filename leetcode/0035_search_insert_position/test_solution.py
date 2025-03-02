import pytest


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        pytest.param([1, 3, 5, 6], 5, 2, id="example 1"),
        pytest.param([1, 3, 5, 6], 2, 1, id="example 2"),
        pytest.param([1, 3, 5, 6], 7, 4, id="example 3"),
        pytest.param([1, 3], 2, 1, id="wrong 1"),
    ],
)
def test_solution(fut, nums, target, expected):
    assert fut(nums, target) == expected
