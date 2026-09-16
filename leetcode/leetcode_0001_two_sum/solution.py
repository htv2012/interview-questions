class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        value2indices = {}
        for i, v in enumerate(nums):
            value2indices.setdefault(v, []).append(i)

        for value, indices in value2indices.items():
            other = target - value
            if value == other:
                if len(indices) == 2:
                    return indices
            elif other in value2indices:
                return [indices[0], value2indices[other][0]]

        raise ValueError(
            "We should not get here. There should be exactly one solution."
        )
