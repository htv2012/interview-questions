"""
In list1, we replace nodes from index a (zero based) to b with list2.

Algorithm
=========
locate the a-1 and b nodes and join list2 in place.

Steps
=====
1. Locate the last node of list2, tail2
2. Traverse list1, keep track of index as if in an array
3. Node(A-1).next = list2
3. tail2.next = Node(B)
"""

from list_node import ListNode


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        # Locate the last node in list2
        tail2 = list2
        while tail2.next is not None:
            tail2 = tail2.next

        node = list1
        count = 0
        while node is not None:
            if count == a - 1:
                # At just before the node to be removed
                node.next, node = list2, node.next
                count += 1
                continue
            elif count == b:
                # At the last node to be removed, merge and done
                tail2.next = node.next
                break

            count += 1
            node = node.next

        return list1
