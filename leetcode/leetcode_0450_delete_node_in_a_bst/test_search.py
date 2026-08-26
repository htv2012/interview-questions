import pytest
from tree import TreeNode, breadth_first_build

from solution import search


@pytest.fixture
def root():
    return breadth_first_build([5, 3, 6, 2, 4, None, 7])


def test_search_empty_node():
    assert search(root=None, key=1, parent=None, side="left") == (None, None, "left")


@pytest.mark.parametrize("key", [5, 3, 6, 2, 4, 7])
def test_search(root, key):
    dummy = TreeNode(-1, left=root)
    found, parent, side = search(root, key, parent=dummy, side="left")
    assert found.val == key
    assert getattr(parent, side) is found
