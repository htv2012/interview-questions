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
