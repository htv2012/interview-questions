class Node(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return 'Node({!r}, {!r})'.format(self.data, self.next)

    def __str__(self):
        return '{}'.format(self.data)


class List(object):
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0
        for item in iterable or []:
            self.append(item)

    def prepend(self, data):
        self.length += 1
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data):
        self.length += 1
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        buffer = ' '.join(str(node) for node in self)
        return buffer

    def __len__(self):
        return self.length
