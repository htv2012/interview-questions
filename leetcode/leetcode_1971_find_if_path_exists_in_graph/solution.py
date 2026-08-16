import collections


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        # Create the graph {node: {neighbors}}
        graph = collections.defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        # Search
        seen = set()  # set of nodes which has been visited
        queue = collections.deque()
        queue.append(source)

        while queue:
            node = queue.popleft()
            if node in seen:
                continue
            seen.add(node)

            for neighbor in graph[node]:
                if neighbor in seen:
                    continue

                if neighbor == destination:
                    return True

                queue.append(neighbor)

        return False
