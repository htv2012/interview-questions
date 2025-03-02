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

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)
        carry = 0
        node = head
        while node is not None:
            carry, node.val = divmod(carry + 2 * node.val, 10)
            if node.next is None and carry > 0:
                node.next = ListNode(carry)
                carry = 0
                break
            node = node.next
        head = self.reverseList(head)
        return head
