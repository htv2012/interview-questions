class Solution:
    def customSortString(self, order: str, s: str) -> str:
        length = len(order)
        order = dict((c, i) for i, c in enumerate(order))
        custom = sorted((order.get(c, length), c) for c in s)
        return "".join(c for i, c in custom)
