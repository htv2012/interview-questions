import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param(
            [3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]], id="example 1"
        ),
        pytest.param([1], [[1]], id="example 2"),
        pytest.param([], [], id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
