import pytest

from solution import tokenize


@pytest.mark.parametrize(
    ["indata", "expected"],
    [
        pytest.param(
            "3[a]2[bc]", ["3", "[", "a", "]", "2", "[", "bc", "]"], id="example 1"
        ),
        pytest.param(
            "3[a2[c]]", ["3", "[", "a", "2", "[", "c", "]", "]"], id="example 2"
        ),
        pytest.param(
            "2[abc]3[cd]ef",
            ["2", "[", "abc", "]", "3", "[", "cd", "]", "ef"],
            id="example 3",
        ),
        pytest.param("100[leetcode]", ["100", "[", "leetcode", "]"], id="wrong 1"),
    ],
)
def test_tokenize(indata, expected):
    # assert tokenize("3[a]") == ["3", "[", "a", "]"]
    assert tokenize(indata) == expected
