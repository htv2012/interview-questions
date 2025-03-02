import pytest


@pytest.mark.parametrize(
    ["positions", "healths", "directions", "expected"],
    [
        pytest.param(
            [5, 4, 3, 2, 1],
            [2, 17, 9, 15, 10],
            "RRRRR",
            [2, 17, 9, 15, 10],
            id="Example 1",
        ),
        pytest.param([3, 5, 2, 6], [10, 10, 15, 12], "RLRL", [14], id="Example 2"),
        pytest.param([1, 2, 5, 6], [10, 10, 11, 11], "RLRL", [], id="Example 3"),
        pytest.param([1, 40], [10, 11], "RL", [10], id="wrong 1"),
        pytest.param([42, 3, 46, 2], [13, 8, 34, 37], "LRLR", [12, 33], id="wrong 2"),
    ],
)
def test_solution(fut, positions, healths, directions, expected):
    assert fut(positions, healths, directions) == expected
