class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        last = None

        for token in tokens:
            try:
                num = int(token)
                if last is not None and num <= last:
                    return False
                last = num
            except ValueError:
                pass

        return True
