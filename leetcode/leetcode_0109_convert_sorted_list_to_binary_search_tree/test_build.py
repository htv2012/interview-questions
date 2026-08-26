from list_node import ListNode

from solution import build


def test_none():
    root = build(None)
    assert root is None


def test_single():
    head = ListNode.from_iterable([1])
    root = build(head)
    assert root.val == 1
    assert root.left is None
    assert root.right is None


def test_double():
    head = ListNode.from_iterable([1, 2])
    root = build(head)

    assert root.val == 2
    assert root.left is not None
    assert root.right is None

    left = root.left
    assert left.val == 1
    assert left.left is None
    assert left.right is None


def test_triple():
    head = ListNode.from_iterable([1, 2, 3])
    root = build(head)
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 3

    assert root.left.left is None
    assert root.left.right is None

    assert root.right.left is None
    assert root.right.right is None


def test_odd():
    head = ListNode.from_iterable([1, 2, 3, 4, 5, 6, 7])
    root = build(head)

    assert root.val == 4
    assert root.left.val == 2
    assert root.right.val == 6

    # Node 1
    assert root.left.left.val == 1
    assert root.left.left.left is None
    assert root.left.left.right is None

    # Node 3
    assert root.left.right.val == 3
    assert root.left.right.left is None
    assert root.left.right.right is None

    # Node 5
    assert root.right.left.val == 5
    assert root.right.left.left is None
    assert root.right.left.right is None

    # Node 7
    assert root.right.right.val == 7
    assert root.right.right.left is None
    assert root.right.right.right is None
