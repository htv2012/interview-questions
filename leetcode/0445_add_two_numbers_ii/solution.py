from typing import Optional

from list_node import ListNode


def list_length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Solution without reversing the lists."""
        # raise NotImplementedError()
        len1 = list_length(l1)
        len2 = list_length(l2)
        out = []

        for _ in range(len1 - len2):
            out.append(l1.val)
            l1 = l1.next
        for _ in range(len2 - len1):
            out.append(l2.val)
            l2 = l2.next

        while l1 is not None:
            n = l1.val + l2.val
            out.append(n)
            l1 = l1.next
            l2 = l2.next

        carry = 0
        for i in range(len(out) - 1, -1, -1):
            carry, out[i] = divmod(out[i] + carry, 10)
        if carry > 0:
            out.insert(0, carry)

        dummy = node = ListNode()
        for value in out:
            node.next = ListNode(value)
            node = node.next
        return dummy.next
