import pytest

"""
394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside
the square brackets is being repeated exactly k times. Note that k is
guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no
extra white spaces, square brackets are well-formed, etc. Furthermore,
you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k. For example, there
will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never
exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

 

Constraints:

    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].


"""


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("3[a]2[bc]", "aaabcbc", id="example 1"),
        pytest.param("3[a2[c]]", "accaccacc", id="example 2"),
        pytest.param("2[abc]3[cd]ef", "abcabccdcdcdef", id="example 3"),
        pytest.param("100[leetcode]", 100 * "leetcode", id="wrong 1"),
        pytest.param(
            "3[z]2[2[y]pq4[2[jk]e1[f]]]ef",
            "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef",
            id="wrong 2",
        ),
        pytest.param("2[a3[b]c]", "abbbcabbbc", id="word found after right bracket"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
