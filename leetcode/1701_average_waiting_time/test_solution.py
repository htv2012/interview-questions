import pytest


@pytest.mark.parametrize(
    ["customers", "expected"],
    [
        pytest.param([[1, 2], [2, 5], [4, 3]], 5.0, id="Example 1"),
        pytest.param([[5, 2], [5, 4], [10, 3], [20, 1]], 3.25, id="Example 2"),
    ],
)
def test_solution(fut, customers, expected):
    assert fut(customers=customers) == expected
