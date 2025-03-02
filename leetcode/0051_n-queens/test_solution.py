import pytest


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(
            4,
            '[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]',
            id="example 1",
        ),
        pytest.param(1, [["Q"]], id="example 2"),
    ],
)
def test_solution(fut, n, expected):
    assert fut(n) == expected
