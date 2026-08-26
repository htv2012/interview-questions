class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        c2w = {}
        w2c = {}
        for ch, word in zip(pattern, words):
            if ch not in c2w and word not in w2c:
                c2w[ch] = word
                w2c[word] = ch

            if c2w.get(ch) != word:
                return False

        return True
