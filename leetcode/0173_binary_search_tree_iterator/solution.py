#!/usr/bin/env python3
# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional

from tree import TreeNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.queue = []
        if root is not None:
            self.queue.append(root)

    def next(self) -> int:
        while self.queue:
            node = self.queue.pop(0)
            if node is not None and not isinstance(node, TreeNode):
                return node

            if node.right is not None:
                self.queue.insert(0, node.right)

            self.queue.insert(0, node.val)

            if node.left is not None:
                self.queue.insert(0, node.left)

    def hasNext(self) -> bool:
        return bool(self.queue)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
