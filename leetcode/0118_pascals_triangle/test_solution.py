import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param(
            5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], id="example 1"
        ),
        pytest.param(1, [[1]], id="example 2"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
