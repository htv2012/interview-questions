"""
https://leetcode.com/problems/number-of-valid-words-in-a-sentence
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "sentence, expected",
    [
        pytest.param("cat and  dog", 3, id="Example 1"),
        pytest.param("!this  1-s b8d!", 0, id="Example 2"),
        pytest.param("alice and  bob are playing stone-game10", 5, id="Example 3"),
        pytest.param("!", 1, id="punctuation only"),
        pytest.param("a!", 1, id="punctuation at the end"),
        pytest.param("c.,", 0, id="more than 1 punctuations"),
        pytest.param("cn,p ", 0, id="comma inside word"),
        # Hyphens
        pytest.param("a-!b", 0, id="hyphen and punctuation together"),
        pytest.param("a-b.", 1, id="hyphen in middle"),
        pytest.param("foo-", 0, id="hyphen at the end"),
        pytest.param("-foo", 0, id="hyphen as first char not allowed"),
    ],
)
def test_solution(sentence, expected):
    sol = Solution()
    assert sol.countValidWords(sentence) == expected
