import collections

from list_node import ListNode


class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        # Place nodes into a stack
        population = []
        node = head
        while node is not None:
            population.append(node)
            node = node.next

        if not population:
            return None

        # Select qualified nodes
        selected = collections.deque([None])
        selected.appendleft(population.pop())
        while population:
            node = population.pop()
            if node.val >= selected[0].val:
                selected.appendleft(node)

        # Fix the next pointers
        for i, node in enumerate(selected, 1):
            if node is not None:
                node.next = selected[i]

        return selected[0]
