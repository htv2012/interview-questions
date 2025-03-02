import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("RD", "Radiant", id="example 1"),
        pytest.param("RDD", "Dire", id="example 2"),
        pytest.param("R", "Radiant", id="single senator"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
