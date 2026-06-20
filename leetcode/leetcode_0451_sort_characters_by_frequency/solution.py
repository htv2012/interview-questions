class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.setdefault(c, 0) + 1
        sorted_freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        return "".join(ch * count for ch, count in sorted_freq)
