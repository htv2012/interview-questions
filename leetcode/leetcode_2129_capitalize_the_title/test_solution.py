"""
https://leetcode.com/problems/capitalize-the-title/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "title, expected",
    [
        pytest.param("capiTalIze tHe titLe", "Capitalize The Title", id="Example 1"),
        pytest.param(
            "First leTTeR of EACH Word", "First Letter of Each Word", id="Example 2"
        ),
        pytest.param("i lOve leetcode", "i Love Leetcode", id="Example 3"),
    ],
)
def test_solution(title, expected):
    sol = Solution()
    assert sol.capitalizeTitle(title) == expected
