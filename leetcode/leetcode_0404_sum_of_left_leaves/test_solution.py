import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([3, 9, 20, None, None, 15, 7], 24, id="example 1"),
        pytest.param([1], 0, id="example 2"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
