import logging

import pytest

"""
49. Group Anagrams
Medium
Topics
Companies

Given an array of strings strs, group the anagrams together. You can
return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters
exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.


"""


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param(
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            id="example 1",
        ),
        pytest.param([""], [[""]], id="example 2"),
        pytest.param(["a"], [["a"]], id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    actual = fut(indata)
    expected = {frozenset(group) for group in expected}
    actual = {frozenset(group) for group in actual}
    logging.debug("actual=%r", actual)
    logging.debug("expected=%r", expected)
    assert actual == expected
