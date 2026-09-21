class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        bound = len(nums) - 1
        nums.sort()

        for i, value in enumerate(nums):
            if value > 0:
                # from here on, all values are positive, we cannot make a sum of zero
                continue
            if i > 0 and value == nums[i - 1]:
                # Skip duplicate of value
                continue

            # Two-sum problem
            left, right = i + 1, bound
            while left < right:
                if (total := value + nums[left] + nums[right]) > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    out.append([value, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return out
