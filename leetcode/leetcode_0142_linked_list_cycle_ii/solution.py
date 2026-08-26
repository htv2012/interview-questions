from list_node import ListNode


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        fast = slow = head
        while True:
            try:
                fast = fast.next.next
            except AttributeError:
                # We reach the end of the list, no cycle
                return None

            slow = slow.next

            if fast is slow:
                break

        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast
