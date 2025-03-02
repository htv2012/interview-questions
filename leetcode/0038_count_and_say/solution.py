import functools
import itertools


class Solution:
    @functools.cache
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prior_result = self.countAndSay(n - 1)
        out = ""
        for value, group in itertools.groupby(prior_result):
            out += f"{len(list(group))}{value}"
        return out
