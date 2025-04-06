import pytest

from main import lonelyinteger


@pytest.mark.parametrize(
    ["a", "expected"],
    [
        pytest.param([1, 2, 3, 4, 3, 2, 1], 4, id="example"),
        pytest.param([1], 1, id="sample0"),
        pytest.param([1, 1, 2], 2, id="sample1"),
        pytest.param([0, 0, 1, 2, 1], 2, id="sample2"),
    ],
)
def test_lonely_integer(a, expected):
    assert lonelyinteger(a) == expected
