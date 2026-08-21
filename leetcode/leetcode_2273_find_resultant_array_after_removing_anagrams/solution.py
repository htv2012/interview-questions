import itertools


def normalize(word):
    return "".join(sorted(word))


class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        out = []
        for _, group in itertools.groupby(words, key=normalize):
            out.append(next(group))
        return out
