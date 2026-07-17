import itertools
import logging
import reprlib
from typing import Optional

logger = logging.getLogger()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        node = self
        while node:
            values.append(node.val)
            node = node.next
        values = reprlib.repr(values)
        return values.replace("[", "<ListNode ").replace("]", ">")

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


def count_nodes(head: Optional[ListNode]) -> int:
    return len(list(iter_list(head)))


def assert_values(head: ListNode, expected: list):
    logger.debug(f"assert_values({head=}, {expected=})")
    node = head
    for node_number, expected_value in enumerate(expected):
        assert node is not None, (
            f"Expect node[{node_number}]={expected_value!r}, but the node is None"
        )
        assert node.val == expected_value, (
            f"Node number: {node_number}, {expected_value=}, {node.val=}"
        )
        node = node.next
    assert node is None


def verify_values(head: Optional[ListNode], expected_values: list) -> bool:
    marker = object()
    pairs = itertools.zip_longest(iter_list(head), expected_values, fillvalue=marker)
    for index, (node, expected_value) in enumerate(pairs):
        if node is marker:
            logger.debug("list is too short, missing %r", expected_values[index:])
            return False
        elif expected_value is marker:
            logger.debug(
                "list is too long, has extra %r", [n.val for n in iter_list(node)]
            )
            return False
        elif node.val != expected_value:
            logger.debug(
                "at node #%d, expected=%r, but actual=%r",
                index,
                expected_value,
                node.val,
            )
            return False
    return True
