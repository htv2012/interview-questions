# https://leetcode.com/problems/merge-sorted-array/description/


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        insertion_point = 0
        for number in nums2:
            # Locate insertion point
            while insertion_point < m and nums1[insertion_point] <= number:
                insertion_point += 1

            # Shift elements right
            for index in range(m, insertion_point, -1):
                nums1[index] = nums1[index - 1]

            # Insert
            nums1[insertion_point] = number
            m += 1
