import pytest


@pytest.mark.parametrize(
    ["numBottles", "numExchange", "expected"],
    [
        pytest.param(9, 3, 13, id="Example 1"),
        pytest.param(15, 4, 19, id="Example 2"),
    ],
)
def test_solution(fut, numBottles, numExchange, expected):
    assert fut(numBottles, numExchange) == expected
