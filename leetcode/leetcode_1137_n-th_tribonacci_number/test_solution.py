import pytest


@pytest.mark.parametrize(
    ["n", "expected"],
    [
        pytest.param(4, 4, id="Example 1"),
        pytest.param(25, 1389537, id="Example 2"),
        pytest.param(37, 2082876103, id="max n"),
    ],
)
def test_solution(fut, n, expected):
    assert fut(n) == expected
