from list_node import ListNode


class Solution:
    def swapNodes(self, head: ListNode | None, k: int) -> ListNode | None:
        # breakpoint()
        # Gets the length of the list
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1

        if k == length - k + 1:
            # node1 and node2 are the same
            return head

        # Locate node1 and node2: the two nodes to swap
        pre_head = ListNode(-1, head)
        prev, node = pre_head, head
        sentinel = object()
        prev1 = node1 = prev2 = node2 = sentinel
        count = 1
        while node is not None:
            if count == k:
                prev1, node1 = prev, node
            elif count == length + 1 - k:
                prev2, node2 = prev, node

            # Optimize by exiting the loop early when both node1 and node2 are accounted for
            if node1 is not sentinel and node2 is not sentinel:
                break

            prev, node = node, node.next
            count += 1

        # swap node1 and node2
        if k == length - k:
            # left- and right node are ajacent
            node1.next = node2.next
            node2.next = node1
            prev1.next = node2
        elif k == length - k + 2:
            # node1 is to the right of- and is adjacent to node2
            node2.next = node1.next
            node1.next = node2
            prev2.next = node1
        else:
            node1.next, node2.next = node2.next, node1.next
            prev1.next, prev2.next = node2, node1

        return pre_head.next
