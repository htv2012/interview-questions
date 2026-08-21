import pytest


@pytest.mark.parametrize(
    ["sentence", "expected"],
    [
        pytest.param(
            "I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa", id="Example 1"
        ),
        pytest.param(
            "The quick brown fox jumped over the lazy dog",
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
            id="Example 2",
        ),
    ],
)
def test_solution(fut, sentence, expected):
    assert fut(sentence) == expected
