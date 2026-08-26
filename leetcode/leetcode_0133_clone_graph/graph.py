class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"<Node {self.val}>"


def from_adj_list(adj_list):
    nodes = {val: Node(val) for val, _ in enumerate(adj_list, 1)}

    for val, nei in enumerate(adj_list, 1):
        node = nodes[val]
        node.neighbors = [nodes[v] for v in nei]

    return nodes[1] if nodes else None


def assert_same_graph(cloned: Node, original: Node):
    done = set()
    que = [(cloned, original)]
    while que:
        n1, n2 = que.pop()
        if n1 is None and n2 is None:
            continue

        if n1.val in done:
            continue

        assert not (n1 is None or n2 is None), f"One of the node is None: {n1} and {n2}"
        assert n1.val == n2.val
        done.add(n1.val)

        assert len(n1.neighbors) == len(n2.neighbors), (
            f"Compare number of neighbors for {n1} and {n2}"
        )
        nei1 = sorted(n1.neighbors, key=lambda n: n.val)
        nei2 = sorted(n2.neighbors, key=lambda n: n.val)
        que.extend(zip(nei1, nei2))
