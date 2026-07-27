from collections.abc import Iterable


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        node = self
        while node:
            values.append(node.val)
            node = node.next
        return f"<ListNode count={len(values)}, nodes={values}>"


def from_iterable(it: Iterable) -> ListNode | None:
    root = None
    prev = None
    node = None
    for value in it:
        node = ListNode(value)
        if prev is None:
            root = node
        else:
            prev.next = node
        prev = node
    return root


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # Edge cases
        if not head:
            return None
        elif head.next is None:
            return head

        # left and right are k nodes apart
        right = head
        try:
            for i in range(k):
                right = right.next
        except AttributeError:
            # k is greater than number of nodes
            k = k % i
            right = head
            for i in range(k):
                right = right.next

        # Check for case when k is equal to the number of nodes:
        if right is None or right == head:
            return head

        left = head
        while right.next:
            left = left.next
            right = right.next

        new_head = left.next
        left.next = None
        right.next = head
        return new_head
