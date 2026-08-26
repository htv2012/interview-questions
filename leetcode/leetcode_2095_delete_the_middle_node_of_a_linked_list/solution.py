from list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        pre_head = ListNode(-1, head)
        prev, tbd, last = pre_head, head, head
        count = 0
        while last is not None:
            last = last.next
            count += 1
            if count % 2 == 0:
                prev = prev.next
                tbd = tbd.next

        if tbd:
            prev.next = tbd.next
        return pre_head.next
