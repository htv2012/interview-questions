def is_palidromic(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def helper(s, left, right):
    if is_palidromic(s, left, right):
        if len(s) % 2 == 0:
            return -1
        return len(s) // 2

    if is_palidromic(s, left + 1, right):
        return left

    if is_palidromic(s, left, right - 1):
        return right

    return -1
    # TODO: missed case?


# What is: the middle of the string is not palidromic?
def palindromeIndex(s):
    return helper(s, left=0, right=len(s) - 1)
