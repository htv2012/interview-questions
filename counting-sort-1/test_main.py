import pytest

from main import countingSort


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        pytest.param([1, 1, 3, 2, 1], {1: 3, 2: 1, 3: 1}, id="example1"),
    ],
)
def test_counting_sort(arr, expected):
    actual = countingSort(arr)
    out = [0] * 100
    for n, count in expected.items():
        out[n] = count
    assert actual == out
