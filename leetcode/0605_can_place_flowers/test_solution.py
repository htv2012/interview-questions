import pytest


@pytest.mark.parametrize(
    "flowerbed, n, expected",
    [
        pytest.param([1, 0, 0, 0, 1], 1, True, id="example 1"),
        pytest.param([1, 0, 0, 0, 1], 2, False, id="example 2"),
        pytest.param([1, 0, 0, 0, 0, 0, 1], 2, True, id="wrong 1"),
        pytest.param([1, 0, 1, 0, 1, 0, 1], 0, True, id="wrong 2"),
    ],
)
def test_solution(fut, flowerbed, n, expected):
    assert fut(flowerbed, n) is expected
