#!/usr/bin/env python3
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-03-13


VOWELS = set("aeiouAEIOU")


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        first = len([c for c in s[:half] if c in VOWELS])
        second = len([c for c in s[half:] if c in VOWELS])
        return first == second
