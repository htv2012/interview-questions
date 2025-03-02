from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<ListNode {self.val}>"

    def __iter__(self):
        node = self
        while node is not None:
            yield node.val
            node = node.next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        step = 0

        while fast is not None:
            fast = fast.next
            step += 1
            if step % 2 == 0:
                slow = slow.next

        if step % 2 == 1:
            slow = slow.next
        return slow
