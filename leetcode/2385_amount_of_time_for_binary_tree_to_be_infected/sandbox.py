#!/usr/bin/env python3
from tree import TreeNode, breadth_first_build

from solution import find


def get_parents(root: TreeNode, parent=None):
    if root is None:
        return
    yield root, parent
    yield from get_parents(root.left, root)
    yield from get_parents(root.right, root)


root = breadth_first_build([1, 2, 3, 4, 5, 6, 7])
f = find(root, 3)
print(f)
