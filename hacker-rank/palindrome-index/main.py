def is_palidromic(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def palindromeIndex(s):
    # Work our way to the middle of the string until a mismatch occurs
    left, right = 0, len(s) - 1
    while left < right and s[left] == s[right]:
        left, right = left + 1, right - 1

    if left >= right:
        # String is palindromic, and the prolem statement
        # said to return -1
        return -1

    if is_palidromic(s, left + 1, right):
        return left

    if is_palidromic(s, left, right - 1):
        return right

    return -1
