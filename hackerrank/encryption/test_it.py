import pytest

from main import encryption


@pytest.mark.parametrize(
    "text, expected",
    [
        pytest.param(
            "if man was meant to stay on the ground god would have given us roots",
            "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau",
            id="example 1",
        ),
        pytest.param("haveaniceday", "hae and via ecy", id="example 2"),
        pytest.param("ab", "a b", id="short"),
        pytest.param("", "", id="empty"),
        pytest.param("chillout", "clu hlt io", id="wrong 1"),
    ],
)
def test_encryption(text, expected):
    assert encryption(text) == expected
