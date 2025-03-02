import pytest


@pytest.mark.parametrize(
    ["board", "click", "expected"],
    [
        pytest.param(
            [
                ["E", "E", "E", "E", "E"],
                ["E", "E", "M", "E", "E"],
                ["E", "E", "E", "E", "E"],
                ["E", "E", "E", "E", "E"],
            ],
            [3, 0],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
            id="example 1",
        ),
        pytest.param(
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
            [1, 2],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "X", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
            id="example 2",
        ),
    ],
)
def test_solution(fut, board, click, expected):
    assert fut(board, click) == expected
