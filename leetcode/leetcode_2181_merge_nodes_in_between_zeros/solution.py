from list_node import ListNode


class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        assert head.val == 0
        node = head.next
        total = 0
        pre_head = tail = ListNode(-1)

        while node is not None:
            if node.val == 0:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0
            else:
                total += node.val
            node = node.next

        return pre_head.next
