import pytest

from main import caesarCipher


@pytest.mark.parametrize(
    ["clear_text", "k", "expected"],
    [
        pytest.param(
            "There's-a-starman-waiting-in-the-sky",
            3,
            "Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb",
            id="example",
        ),
        pytest.param(
            "abcdef",
            26,
            "abcdef",
            id="shift full width",
        ),
    ],
)
def test_caesarCipher(clear_text, k, expected):
    assert caesarCipher(clear_text, k) == expected
