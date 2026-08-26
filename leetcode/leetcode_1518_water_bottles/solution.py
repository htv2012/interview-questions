class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles_count = numBottles
        unexchanged = 0
        while numBottles != 0:
            numBottles, unexchanged = divmod(numBottles + unexchanged, numExchange)
            bottles_count += numBottles
        return bottles_count
