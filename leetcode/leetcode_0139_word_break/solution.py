# https://leetcode.com/problems/word-break/description/


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        found = [False] * len(s) + [True]

        for index in range(len(s) - 1, -1, -1):
            # if i == 0:
            for word in wordDict:
                word_length = len(word)
                if s[index : index + word_length] == word:
                    found[index] = found[index + word_length]
                if found[index]:
                    break

        return found[0]
