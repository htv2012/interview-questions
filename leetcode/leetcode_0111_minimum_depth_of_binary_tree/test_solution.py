import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([3, 9, 20, None, None, 15, 7], 2, id="example 1"),
        pytest.param([2, None, 3, None, 4, None, 5, None, 6], 5, id="example 2"),
        pytest.param([], 0, id="wrong 1"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
