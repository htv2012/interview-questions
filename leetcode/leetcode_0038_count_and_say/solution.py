import functools
import itertools


@functools.cache
def count_and_say(n: int) -> str:
    if n == 1:
        return "1"

    prior_result = count_and_say(n - 1)
    out = ""
    for value, group in itertools.groupby(prior_result):
        out += f"{len(list(group))}{value}"
    return out


class Solution:
    def countAndSay(self, n: int) -> str:
        return count_and_say(n)
