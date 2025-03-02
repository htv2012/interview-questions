# test_height.py
import pytest
from tree import TreeNode

from solution import height


def generate_test_cases():
    yield pytest.param(None, 0, id="none")
    yield pytest.param(TreeNode(1), 1, id="single node")
    yield pytest.param(TreeNode(1, left=TreeNode(2)), 2, id="2 nodes")
    yield pytest.param(
        TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
        2,
        id="3 balanced nodes",
    )

    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))
    yield pytest.param(root, 3, id="3 nodes linked list formation, left")

    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
    yield pytest.param(root, 3, id="3 nodes linked list formation, right")


@pytest.mark.parametrize("root, expected", generate_test_cases())
def test_height(root, expected):
    assert height(root) == expected
