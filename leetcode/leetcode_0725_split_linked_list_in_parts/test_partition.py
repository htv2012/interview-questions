import pytest

from solution import partition


@pytest.mark.parametrize(
    "n, k, expected", [(8, 3, [3, 6, 8]), (7, 3, [3, 5, 7]), (3, 5, [1, 2, 3, 3, 3])]
)
def test_partition(n, k, expected):
    assert list(partition(n, k)) == expected
