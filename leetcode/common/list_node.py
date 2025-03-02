class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # return f"<ListNode {self.val}>"
        values = []
        node = self
        while node:
            values.append(node.val)
            node = node.next
        return f"<ListNode val={self.val}, nodes={values}>"

    def __iter__(self):
        node = self
        while node is not None:
            yield node.val
            node = node.next

    def __eq__(self, other: object) -> bool:
        me = self
        while me is not None and other is not None and me.val == other.val:
            me = me.next
            other = other.next
        return me is None and other is None

    @classmethod
    def from_iterable(cls, it):
        root = None
        prev = None
        node = None
        for value in it:
            node = cls(value)
            if prev is None:
                root = node
            else:
                prev.next = node
            prev = node
        return root


def iter_list(head: ListNode):
    while head is not None:
        yield head
        head = head.next


def assert_values(head: ListNode, expected: list):
    node = head
    for node_number, expected_value in enumerate(expected):
        assert (
            node.val == expected_value
        ), f"Node number: {node_number}, {expected_value=}, {node.val=}"
        node = node.next
    assert node is None
