def has_cycle(head):
    fast = slow = head
    steps = 0
    while fast is not None:
        fast = fast.next
        steps += 1

        if fast is slow:
            return 1

        if steps % 2 == 0:
            slow = slow.next

    return 0
