class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


def removeDuplicates(llist):
    if llist is None:
        return None

    left, right = llist, llist.next
    while right is not None:
        if right.data != left.data:
            left.next = right
            left = left.next
        right = right.next
    left.next = None
    return llist
