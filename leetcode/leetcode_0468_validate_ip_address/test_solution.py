"""
https://leetcode.com/problems/validate-ip-address/
"""

from types import SimpleNamespace

import pytest

from solution import Solution


def ns(queryIP: str, expected: str) -> SimpleNamespace:
    return SimpleNamespace(queryIP=queryIP, expected=expected)


@pytest.fixture
def fut():
    sol = Solution()
    return sol.validIPAddress


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            ns(queryIP="172.16.254.1", expected="IPv4"),
            id="Example 1",
        ),
        pytest.param(
            ns(queryIP="2001:0db8:85a3:0:0:8A2E:0370:7334", expected="IPv6"),
            id="Example 2",
        ),
        pytest.param(
            ns(queryIP="256.256.256.256", expected="Neither"),
            id="Example 3",
        ),
        pytest.param(
            ns(queryIP="192.168.1.0", expected="IPv4"),
            id="valid IPv4 1",
        ),
        pytest.param(
            ns(queryIP="10.10.10.10", expected="IPv4"),
            id="valid IPv4 2",
        ),
        pytest.param(
            ns(queryIP="192.168.01.1", expected="Neither"),
            id="leading zero not allowed",
        ),
        pytest.param(
            ns(queryIP="192.168@1.1", expected="Neither"),
            id="invalid separator",
        ),
        pytest.param(
            ns(queryIP="2001:0db8:85a3::8A2E:037j:7334", expected="Neither"),
            id="incorrect length",
        ),
        pytest.param(
            ns(queryIP="02001:0db8:85a3:0000:0000:8a2e:0370:7334", expected="Neither"),
            id="5-digit numbers not allowed",
        ),
        pytest.param(ns(queryIP="", expected="Neither"), id="empty string"),
        pytest.param(
            ns(queryIP="2001:db8:85a3:0::8a2E:0370:7334", expected="Neither"),
            id="empty num",
        ),
    ],
)
def test_solution(fut, test_case):
    assert fut(test_case.queryIP) == test_case.expected
