from typing import Optional

from list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while head is not None:
            # Count the number of nodes with the same value
            count = 1
            node = head.next
            while node is not None and node.val == head.val:
                node = node.next
                count += 1

            # Only keep those which are not duplicated
            if count == 1:
                tail.next = ListNode(head.val)
                tail = tail.next

            # Advance
            head = node

        return dummy.next
