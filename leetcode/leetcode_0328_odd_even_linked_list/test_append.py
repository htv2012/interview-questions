from list_node import ListNode, assert_values

from solution import append_node


def test_append_to_list_of_0_element():
    node = ListNode(9)
    assert node.val == 9
    assert node.next is None

    head, tail = append_node(None, None, node)

    assert head is node
    assert tail is node
    assert node.val == 9
    assert node.next is None


def test_append_to_list_of_1_element():
    head = tail = ListNode(1)
    node = ListNode(2)

    new_head, new_tail = append_node(head, tail, node)
    assert new_head is head
    assert new_head.next is new_tail
    assert new_tail is node


def test_append_to_list_of_2_elements():
    tail = ListNode(2)
    head = ListNode(1, tail)
    node = ListNode(3)

    new_head, new_tail = append_node(head, tail, node)

    assert new_head is head
    assert tail.next is new_tail


def test_append_to_list_of_3_elements():
    head = ListNode.from_iterable([1, 2, 3])
    tail = head.next.next
    assert_values(head, [1, 2, 3])

    new_head, new_tail = append_node(head, tail, ListNode(4))

    assert new_head is head
    assert tail.next is new_tail
    assert_values(head, [1, 2, 3, 4])
