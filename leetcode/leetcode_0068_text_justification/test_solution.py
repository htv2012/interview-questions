import pytest


@pytest.mark.parametrize(
    "words, maxWidth, expected",
    [
        pytest.param(
            ["This", "is", "an", "example", "of", "text", "justification."],
            16,
            [
                "This    is    an",
                "example  of text",
                "justification.  ",
            ],
            id="example 1",
        ),
        pytest.param(
            ["What", "must", "be", "acknowledgment", "shall", "be"],
            16,
            [
                "What   must   be",
                "acknowledgment  ",
                "shall be        ",
            ],
            id="example 2",
        ),
        pytest.param(
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ",
            ],
            id="example 3",
        ),
        pytest.param(
            ["Listen", "to", "many,", "speak", "to", "a", "few."],
            6,
            [
                "Listen",
                "to    ",
                "many, ",
                "speak ",
                "to   a",
                "few.  ",
            ],
            id="wrong 1",
        ),
    ],
)
def test_solution(fut, words, maxWidth, expected):
    assert fut(words, maxWidth) == expected
