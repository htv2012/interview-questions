class Solution:
    def pivotInteger(self, n: int) -> int:
        left_index, right_index = 1, n
        left_sum, right_sum = 1, n
        while left_index <= right_index:
            if left_sum < right_sum:
                left_index += 1
                left_sum += left_index
            elif left_sum > right_sum:
                right_index -= 1
                right_sum += right_index
            elif left_index == right_index:
                # Both sums are equal, and indices are equal: found it
                return left_index
            else:
                # Both sums are equal, but indices are still apart
                left_index += 1
                left_sum += left_index
                right_index -= 1
                right_sum += right_index

        return -1
