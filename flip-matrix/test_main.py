import pytest

from main import flippingMatrix


@pytest.mark.parametrize(
    ["matrix", "expected"],
    [
        pytest.param([[1, 2], [3, 4]], 4, id="example0"),
        pytest.param(
            [
                [112, 42, 114, 119],
                [56, 125, 101, 49],
                [15, 78, 56, 43],
                [62, 98, 83, 108],
            ],
            414,
            id="example1",
        ),
    ],
)
def test_flipping_matrix(matrix, expected):
    assert flippingMatrix(matrix) == expected
