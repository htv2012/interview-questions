def get_length(head):
    count = 0
    node = head
    while node is not None:
        count += 1
        node = node.next
    return count


def advance(head, count):
    node = head
    for _ in range(count):
        node = node.next
    return node


def findMergeNode(head1, head2) -> int:
    len1 = get_length(head1)
    len2 = get_length(head2)

    node1 = advance(head1, len1 - len2)
    node2 = advance(head2, len2 - len1)

    while node1 is not None:
        if node1 is node2:
            return node1.data
        node1 = node1.next
        node2 = node2.next

    raise ValueError()
