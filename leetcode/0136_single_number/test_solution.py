import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([2, 2, 1], 1, id="example 1"),
        pytest.param([4, 1, 2, 1, 2], 4, id="example 2"),
        pytest.param([1], 1, id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
