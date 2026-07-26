from list_node import ListNode


class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        # pre_head a dummy node, points to the new head
        pre_head = ListNode(-1)

        node = head
        while node is not None:
            next_node = node.next

            # Find the right insertion point
            left, right = pre_head, pre_head.next
            while right is not None and right.val < node.val:
                left, right = right, right.next

            # Insert new node between left and right pointers
            left.next = node
            node.next = right

            node = next_node

        return pre_head.next
