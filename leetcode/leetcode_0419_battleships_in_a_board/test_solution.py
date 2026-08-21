import pytest


@pytest.mark.parametrize(
    ["board", "expected"],
    [
        pytest.param(
            [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]],
            2,
            id="Example 1",
        ),
        pytest.param([["."]], 0, id="Example 2"),
        pytest.param(
            [
                [".", "X", "X", "X", "."],
                [".", ".", ".", ".", "."],
                [".", "X", "X", "X", "X"],
            ],
            2,
            id="my 1",
        ),
    ],
)
def test_solution(fut, board, expected):
    pass
