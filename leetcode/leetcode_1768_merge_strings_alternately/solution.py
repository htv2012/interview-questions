class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # return "".join(c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue=""))
        result = "".join(c1 + c2 for c1, c2 in zip(word1, word2))
        if (len1 := len(word1)) < (len2 := len(word2)):
            result += word2[len1:]
        elif len2 < len1:
            result += word1[len2:]
        return result
