import pytest


@pytest.mark.parametrize(
    ["n", "expected"],
    [
        pytest.param(13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], id="Example 1"),
        pytest.param(2, [1, 2], id="Example 2"),
    ],
)
def test_solution(fut, n, expected):
    pass
