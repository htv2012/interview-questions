import pytest
import tree
from drawtree.drawtree import drawtree


@pytest.mark.parametrize(
    "root, expected",
    [
        pytest.param(
            "[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]",
            "[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]",
            id="example 1",
        ),
        pytest.param("[0,null,1]", "[1,null,1]", id="example 2"),
    ],
)
def test_solution(fut, root, expected):
    root = tree.deserialize(root)
    print("root:")
    drawtree(root)

    expected_tree = tree.deserialize(expected)
    print("expected:")
    drawtree(expected_tree)

    greater_tree = fut(root)
    print("greater_tree:")
    drawtree(greater_tree)
    actual = tree.serialize(greater_tree)

    assert actual == expected
