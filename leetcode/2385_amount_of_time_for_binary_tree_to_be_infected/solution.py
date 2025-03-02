#!/usr/bin/env python3
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/?envType=daily-question&envId=2024-03-13
from typing import Optional

from tree import TreeNode


def set_parent(root: Optional[TreeNode], parent: Optional[TreeNode] = None):
    if root is None:
        return
    setattr(root, "parent", parent)
    set_parent(root.left, root)
    set_parent(root.right, root)


def find(root: Optional[TreeNode], value) -> Optional[TreeNode]:
    if root is None:
        return None
    elif root.val == value:
        return root
    elif found := find(root.left, value):
        return found
    elif found := find(root.right, value):
        return found
    return None


def get_parents(root: TreeNode, parent=None):
    if root is None:
        return
    yield root, parent
    yield from get_parents(root.left, root)
    yield from get_parents(root.right, root)


def spread(root: Optional[TreeNode], parent, infected: dict):
    if root is None:
        return
    

    local_infected = {}
    if infected.get(root.left, False):
        local_infected[root] = True
    if infected.get(root.right, False):
        local_infected[root] = True
    if infected.get(parent, False):
        local_infected[root] = True
    

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = dict(get_parents(root))
        infected = {node: False for node in parents}
        start = find(root, start)
        infected[start] = True
        time = 0

        while not all(infected.values()):


        return parents
