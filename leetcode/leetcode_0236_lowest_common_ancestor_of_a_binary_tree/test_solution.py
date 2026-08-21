import pytest
import tree
from drawtree.drawtree import drawtree


@pytest.mark.parametrize(
    "root, p, q, expected",
    [
        pytest.param([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3, id="example 1"),
        pytest.param([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5, id="example 2"),
    ],
)
def test_solution(fut, root, p, q, expected):
    root = tree.breadth_first_build(root)
    print("\nroot:")
    drawtree(root)
    for node in tree.inorder_iter(root):
        if node.val == p:
            p = node
        if node.val == q:
            q = node
        if node.val == expected:
            expected = node

    assert isinstance(p, tree.TreeNode)
    assert isinstance(q, tree.TreeNode)
    assert isinstance(expected, tree.TreeNode)
    assert fut(root, p, q) is expected
