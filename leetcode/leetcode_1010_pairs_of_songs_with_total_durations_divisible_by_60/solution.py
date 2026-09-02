class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        mod = [0] * 60
        count = 0
        for duration in time:
            rem = duration % 60
            if rem == 0:
                count += mod[0]
            else:
                count += mod[60 - rem]
            mod[rem] += 1
        return count
