import pytest

from main import miniMaxSum


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        pytest.param([1, 3, 5, 7, 9], "16 24\n", id="example"),
        pytest.param([1, 2, 3, 4, 5], "10 14\n", id="sample0"),
        pytest.param([7, 69, 2, 221, 8974], "299 9271\n", id="sample1"),
    ],
)
def test_mini_max_sum(arr, expected, capfd):
    miniMaxSum(arr)
    actual = capfd.readouterr().out
    assert actual == expected
