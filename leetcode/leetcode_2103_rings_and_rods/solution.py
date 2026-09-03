class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        i = 0

        while i < len(rings):
            color, num = rings[i : i + 2]
            rods[int(num)].add(color)
            i += 2

        return rods.count({"R", "G", "B"})
