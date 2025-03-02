from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples_count = sum(apple)
        capacity.sort(reverse=True)
        for boxes_count, box_capacity in enumerate(capacity, 1):
            apples_count -= box_capacity
            if apples_count <= 0:
                return boxes_count
        raise ValueError()
