import collections
import statistics
from typing import List, Optional

from tree import TreeNode


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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        out = []
        for node, level in breadth_first_iter(root):
            while len(out) <= level:
                out.append([])
            out[level].append(node.val)
        averages = [statistics.mean(row) for row in out]
        return averages
