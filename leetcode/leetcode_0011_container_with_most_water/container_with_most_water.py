class Solution:
    def maxArea(self, height: list[int]) -> int:
        most = 0
        left, right = 0, len(height) - 1
        while left < right:
            left_height, right_height = height[left], height[right]
            capacity = (right - left) * min(left_height, right_height)
            most = max(most, capacity)

            # Move the shorter height. If they are the same, move both ends
            if left_height < right_height:
                left += 1
            elif left_height > right_height:
                right -= 1
            else:
                left += 1
                right -= 1

        return most
