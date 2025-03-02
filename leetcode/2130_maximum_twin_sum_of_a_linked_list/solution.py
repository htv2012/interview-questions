from typing import Optional

from list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, current_node = None, head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node

    def pairSum(self, head: Optional[ListNode]) -> int:
        # Prepare: find the mid point, reverse the second half
        mid = tail = head
        count = 1
        while tail.next:
            tail = tail.next
            count += 1
            if count % 2 == 1:
                mid = mid.next
        mid.next = head2 = self.reverseList(mid.next)

        # Start calculating
        out = head.val + head2.val
        while head2:
            out = max(out, head.val + head2.val)
            head = head.next
            head2 = head2.next

        # Clean up and go
        mid.next = self.reverseList(mid.next)
        return out
