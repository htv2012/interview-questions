#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "word, words, expected",
    [
        pytest.param("leetcode", ["leet", "code"], True, id="example 1"),
        pytest.param("applepenapple", ["apple", "pen"], True, id="example 2"),
        pytest.param(
            "catsandog", ["cats", "dog", "sand", "and", "cat"], False, id="example 3"
        ),
        pytest.param("foobar", ["foo", "fo", "obar"], True, id="my 1"),
        pytest.param(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
            False,
            id="wrong 1",
        ),
        pytest.param(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            [
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
                "ba",
            ],
            False,
            id="wrong 2",
        ),
        pytest.param("abcd", ["a", "abc", "b", "cd"], True, id="wrong 3"),
    ],
)
def test_solution(fut, word, words, expected):
    assert fut(s=word, wordDict=words) is expected
