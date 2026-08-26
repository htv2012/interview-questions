import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([2, 1, 3], 1, id="example 1"),
        pytest.param([1, 2, 3, 4, None, 5, 6, None, None, 7], 7, id="example 2"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
