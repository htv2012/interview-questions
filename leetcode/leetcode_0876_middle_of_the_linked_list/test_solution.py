import pytest

from solution import ListNode, Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.middleNode


def build(seq: list):
    dummy = ListNode()
    tail = dummy
    for value in seq:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def generate_cases():
    for i in range(1, 101):
        seq = list(range(1, i + 1))
        mid = i // 2
        expected = seq[mid:]
        test_id = f"{i=}, expected={mid}"
        yield pytest.param(seq, expected, id=test_id)


@pytest.mark.parametrize(
    "head, expected",
    [
        pytest.param([1, 2, 3, 4, 5], [3, 4, 5], id="example 1"),
        pytest.param([1, 2, 3, 4, 5, 6], [4, 5, 6], id="example 2"),
        pytest.param([1], [1], id="edge: len=1"),
        pytest.param([1, 2], [2], id="edge: len=2"),
    ]
    + list(generate_cases()),
)
def test_solution(head, expected, fut):
    head = build(head)
    middle = fut(head)
    assert list(middle) == expected
