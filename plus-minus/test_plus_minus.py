import pytest

from main import plusMinus


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        pytest.param([1, 1, 0, -1, -1], "0.400000\n0.400000\n0.200000\n", id="example"),
        pytest.param(
            [-4, 3, -9, 0, 4, 1], "0.500000\n0.333333\n0.166667\n", id="sample0"
        ),
        pytest.param(
            [1, 2, 3, -1, -2, -3, 0, 0], "0.375000\n0.375000\n0.250000\n", id="sample1"
        ),
    ],
)
def test_plus_minus(arr, expected, capfd):
    plusMinus(arr)
    actual = capfd.readouterr().out
    assert actual == expected
