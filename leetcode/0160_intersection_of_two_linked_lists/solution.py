from typing import Optional

from list_node import ListNode


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        def _advance(node, wrap):
            if node is None:
                return wrap
            return node.next

        nodea, nodeb = headA, headB
        while nodea is not nodeb:
            nodea = _advance(nodea, headB)
            nodeb = _advance(nodeb, headA)
        return nodea
