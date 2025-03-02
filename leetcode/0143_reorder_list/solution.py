import collections
from typing import Optional

# import pysnooper
from list_node import ListNode


# @pysnooper.snoop("/tmp/snoop.txt")
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Place all nodes into a queue
        queue = collections.deque()
        node = head
        while node is not None:
            queue.append(node)
            node = node.next

        node = ListNode()
        i = 0
        popper = [queue.popleft, queue.pop]

        while queue:
            node.next = popper[i]()

            # Alternate between 0 and 1, or popleft and pop
            i = 1 - i

            node = node.next
        node.next = None
