import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2], id="example 1"),
        pytest.param([2, 0, 1], [0, 1, 2], id="example 2"),
    ],
)
def test_solution(fut, indata, expected):
    fut(indata)
    assert indata == expected
