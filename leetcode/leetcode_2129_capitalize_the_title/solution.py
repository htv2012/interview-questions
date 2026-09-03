class Solution:
    def capitalizeTitle(self, title: str) -> str:
        out = " ".join(w.lower() if len(w) <= 2 else w.title() for w in title.split())
        return out
