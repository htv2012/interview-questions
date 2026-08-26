class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trusted = dict.fromkeys(range(1, n + 1), 0)
        disqualified = set()

        for a, b in trust:
            disqualified.add(a)
            trusted[b] += 1

        for person, trust_count in trusted.items():
            if trust_count == n - 1 and person not in disqualified:
                return person

        return -1
