import nary_tree
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("[1,null,3,2,4,null,5,6]", 3, id="example 1"),
        pytest.param(
            "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]",
            5,
            id="example 2",
        ),
    ],
)
def test_solution(fut, indata, expected):
    root = nary_tree.deserialize(indata)
    assert fut(root) == expected
