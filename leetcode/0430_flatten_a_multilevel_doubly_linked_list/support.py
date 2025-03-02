import itertools
import logging

logging.basicConfig(level="DEBUG")


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __repr__(self):
        values = []
        node = self
        count = 0
        while node:
            if node.child:
                value = f"*{node.val}"
            else:
                value = f" {node.val}"
            values.append(value)
            count += 1
            node = node.next
        values = ", ".join(values)
        return f":<len={count}, values=[{values}]>"


def from_iter(it):
    dummy = Node(-1, None, None, None)
    node = dummy
    for value in it:
        if value is None:
            break
        node.next = Node(value, prev=node, next=None, child=None)
        node = node.next
    if dummy is not node:
        dummy.next.prev = None
    return dummy.next


def iter_list(node):
    while node:
        yield node
        node = node.next


def create_multi_tier(values):
    values = iter(values)
    head = from_iter(values)
    logging.debug("in multi tier, head=%r", head)
    if head is None:
        return
    node = head
    for value in values:
        if value is not None:
            values = itertools.chain([value], values)
            break
        node = node.next
    logging.debug("in multi tier, node=%r", node)
    node.child = create_multi_tier(values)
    return head


def format_multi_tier(head: Node, level: int = 0):
    if head is None:
        return ""

    # TODO: implement
