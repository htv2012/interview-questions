"""
https://leetcode.com/problems/reverse-prefix-of-word/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "word, ch, expected",
    [
        pytest.param("abcdefd", "d", "dcbaefd", id="Example 1"),
        pytest.param("xyxzxe", "z", "zxyxxe", id="Example 2"),
        pytest.param("abcd", "z", "abcd", id="Example 3"),
        pytest.param("abc", "c", "cba", id="reverse all"),
        pytest.param("abcdef", "a", "abcdef", id="reverse first char"),
    ],
)
def test_solution(word, ch, expected):
    sol = Solution()
    assert sol.reversePrefix(word, ch) == expected
