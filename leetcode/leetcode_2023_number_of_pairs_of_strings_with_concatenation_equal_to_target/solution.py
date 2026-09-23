class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        count = 0
        counter = {}

        for i, value in enumerate(nums):
            prefix = target.removesuffix(value)
            if prefix + value == target:
                count += counter.get(prefix, 0)

            suffix = target.removeprefix(value)
            if value + suffix == target:
                count += counter.get(suffix, 0)

            counter[value] = counter.setdefault(value, 0) + 1

        return count
