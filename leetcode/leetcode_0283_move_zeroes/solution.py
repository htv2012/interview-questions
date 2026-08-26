class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zcount = nums.count(0)
        if zcount == 0 or zcount == len(nums):
            return

        left = 0
        for right, value in enumerate(nums):
            if value != 0 and left != right:
                nums[left] = value
            if value != 0:
                left += 1

        nums[-zcount:] = [0] * zcount
