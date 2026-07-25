from list_node import ListNode


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        discard_set = set(nums)
        pre_head = tail = ListNode(-1, head)

        node = head
        while node is not None:
            next_node = node.next
            if node.val not in discard_set:
                tail.next = node
                tail = node
                node.next = None
            node = next_node

        return pre_head.next
