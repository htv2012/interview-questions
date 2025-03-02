from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        found = set()
        for number in arr:
            if number in found:
                return True
            found.add(number * 2)
            if number % 2 == 0:
                found.add(number // 2)
        return False
