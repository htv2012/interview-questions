import logging
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        left, right = None, head
        while right is not None:
            logging.debug("head, left, right = %r, %r, %r", head, left, right)
            if right.val == val:
                if left is None:
                    logging.debug("delete %r from head %r", val, head)
                    head = right.next
                    left, right = None, head
                else:
                    logging.debug("delete %r from %r", val, right)
                    left.next = right.next
                    left = right.next
                    right = left.next
            else:
                left, right = right, right.next

        logging.debug("finally, head=%r", head)
        return head
