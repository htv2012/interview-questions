import logging
import random

from list_node import build, iter_list

from main import findMergeNode

logging.basicConfig(level="DEBUG")
logger = logging.getLogger()


def generate():
    values1 = list(range(random.randint(5, 30)))
    random.shuffle(values1)
    logger.debug(f"{values1=}")
    head1 = build(values1)
    merge_node = head1
    while merge_node.data != 0:
        merge_node = merge_node.next

    values2 = list(range(1, random.randint(5, 10)))
    random.shuffle(values2)
    logger.debug(f"{values2=}")
    head2 = build(values2)
    tail = head2
    while tail.next is not None:
        tail = tail.next

    tail.next = merge_node

    logger.debug(f"head1: {[n.val for n in iter_list(head1)]}")
    logger.debug(f"head2: {[n.val for n in iter_list(head2)]}")

    return head1, head2


def test_find_merge_node():
    head1, head2 = generate()
    assert findMergeNode(head1, head2) == 0
    assert findMergeNode(head2, head1) == 0
