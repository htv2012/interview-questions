from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = 0
        reader = 0
        bound = len(chars)

        while reader < bound:
            chars[writer] = chars[reader]
            count = 0
            while reader < bound and chars[reader] == chars[writer]:
                reader += 1
                count += 1

            writer += 1
            if count != 1:
                for c in str(count):
                    chars[writer] = c
                    writer += 1
        return writer
