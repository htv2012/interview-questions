import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([3, 9, 20, None, None, 15, 7], True, id="example 1"),
        pytest.param([1, 2, 2, 3, 3, None, None, 4, 4], False, id="example 2"),
        pytest.param([], True, id="example 3"),
        pytest.param(
            [1, 2, 2, 3, None, None, 3, 4, None, None, 4], False, id="wrong 1"
        ),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
