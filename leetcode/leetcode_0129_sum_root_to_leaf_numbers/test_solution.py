import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 2, 3], 25, id="example 1"),
        pytest.param([4, 9, 0, 5, 1], 1026, id="example 1"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
