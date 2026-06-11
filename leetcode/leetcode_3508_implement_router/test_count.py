import pytest

from testlib import t


def test_empty(router):
    assert router.getCount(1, 1, 1) == 0
    assert router.getCount(5, 11, 13) == 0


@pytest.mark.parametrize(
    "test_case",
    [
        t("return single", args=(2, 5, 7), expected=1),
        t("return multiple", args=(2, 5, 9), expected=2),
        t("outside of window", args=(2, 1, 4), expected=0),
    ],
)
def test_get_count(router, test_case):
    assert router.getCount(*test_case.args) == test_case.expected
