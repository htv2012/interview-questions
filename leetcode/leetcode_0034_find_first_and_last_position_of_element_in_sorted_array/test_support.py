import pytest

from solution import find_first


@pytest.mark.parametrize(
    ["nums", "target", "left", "right", "expected"],
    [
        pytest.param([1, 2, 2, 2, 3, 4], 2, 0, 2, 1, id="Example 1"),
    ],
)
def test_find_first(nums, target, left, right, expected):
    assert find_first(nums, target, left, right) == expected
