class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean up
        chars = [ch for ch in s.lower() if ch.isalnum()]

        # Compare chars from both ends into the middle
        # Also handle cases when string is empty
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True
