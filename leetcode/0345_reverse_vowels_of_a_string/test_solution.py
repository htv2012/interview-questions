import pytest

"""
345. Reverse Vowels of a String
Easy

Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.


"""


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("hello", "holle", id="example 1"),
        pytest.param("leetcode", "leotcede", id="example 2"),
        pytest.param("aA", "Aa", id="wrong 1"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
