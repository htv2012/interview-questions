import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("A", 1, id="example 1"),
        pytest.param("AB", 28, id="example 2"),
        pytest.param("ZY", 701, id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
