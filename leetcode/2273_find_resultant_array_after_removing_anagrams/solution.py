import itertools
from typing import List


def normalize(word):
    return "".join(sorted(word))


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        out = []
        for _, group in itertools.groupby(words, key=normalize):
            out.append(next(group))
        return out
