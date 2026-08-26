from list_node import ListNode


class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        # Place nodes into a monotonic stack
        stack = []
        node = head
        while node is not None:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next

        stack.append(None)
        for i, node in enumerate(stack, 1):
            if node is not None:
                node.next = stack[i]

        return stack[0]
