import collections
import logging

from tree import TreeNode

logger = logging.getLogger()


def breadth_first_iter(node: TreeNode, level: int = 0):
    queue = collections.deque([(node, level)])
    while queue:
        node, level = queue.popleft()
        if node is None:
            continue
        yield node, level
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        out = []
        for node, level in breadth_first_iter(root):
            logger.debug("node=%r, level=%d", node, level)
            while level >= len(out):
                out.append([])
            out[level].append(node.val)
        out.reverse()
        return out
