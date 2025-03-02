import collections
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """Find center of the star graph.

        Strategy: Just cound the node IDs. The one that is repeated the
        most is the center.
        """
        counter = collections.Counter()
        for edge in edges:
            counter.update(edge)

        node_id = counter.most_common(1)[0][0]
        return node_id
