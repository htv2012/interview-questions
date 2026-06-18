class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        t1 = [int(x) for x in version1.split(".")]
        t2 = [int(x) for x in version2.split(".")]
        
        max_len = max(len(t1), len(t2))
        t1.extend([0] * (max_len - len(t1)))
        t2.extend([0] * (max_len - len(t2)))

        for a, b in zip(t1, t2):
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0
