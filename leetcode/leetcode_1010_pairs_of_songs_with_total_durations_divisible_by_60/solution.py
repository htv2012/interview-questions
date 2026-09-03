TARGET = 60


class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        remainders = [0] * TARGET
        count = 0
        for duration in time:
            remainder = duration % TARGET
            count += remainders[(TARGET - remainder) % TARGET]
            remainders[remainder] += 1
        return count
