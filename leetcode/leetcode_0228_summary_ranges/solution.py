from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        out = []
        it = iter(nums)
        first = last = next(it)
        for num in it:
            if num - last > 1:
                range_ = str(first) if first == last else f"{first}->{last}"
                out.append(range_)
                first = num

            last = num

        range_ = str(first) if first == last else f"{first}->{last}"
        out.append(range_)

        return out
