from typing import List, Optional

from tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = []
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)
            if node is None:
                continue

            while len(right_side) <= level:
                right_side.append(None)
            right_side[level] = node.val

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return right_side
