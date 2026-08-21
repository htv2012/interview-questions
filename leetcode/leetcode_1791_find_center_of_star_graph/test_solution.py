import pytest


@pytest.mark.parametrize(
    ["edges", "expected"],
    [
        pytest.param([[1, 2], [2, 3], [4, 2]], 2, id="Example 1"),
        pytest.param([[1, 2], [5, 1], [1, 3], [1, 4]], 1, id="Example 2"),
    ],
)
def test_solution(fut, edges, expected):
    assert fut(edges) == expected
