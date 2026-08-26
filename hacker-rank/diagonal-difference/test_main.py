import pytest

from main import diagonalDifference


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        pytest.param([[1, 2, 3], [4, 5, 6], [9, 8, 9]], 2, id="example1"),
        pytest.param([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15, id="sample0"),
    ],
)
def test_diagonal_difference(arr, expected):
    assert diagonalDifference(arr) == expected
