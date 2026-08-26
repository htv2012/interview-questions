import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([5, 2, -3], [2, -3, 4], id="example 1"),
        pytest.param([5, 2, -5], [2], id="example 2"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
