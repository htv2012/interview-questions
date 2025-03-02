#!/usr/bin/env python
"""
Given two linked lists representing the digits from two numbers, write
an add function to return a linked list representing the sum.
"""

from __future__ import print_function
from linked_list import List


def add(list1, list2):
    it1 = iter(list1)
    it2 = iter(list2)

    reversed_sum = List()  # Reversed sum
    length_difference = len(list1) - len(list2)
    for _ in range(length_difference):
        reversed_sum.prepend(it1.next().data)
    for _ in range(-length_difference):
        reversed_sum.prepend(it2.next().data)

    for node1, node2 in zip(it1, it2):
        reversed_sum.prepend(node1.data + node2.data)

    sum_list = List()
    carry = 0
    for node in reversed_sum:
        value = node.data + carry
        value, carry = value % 10, value // 10
        sum_list.prepend(value)
    if carry:
        sum_list.prepend(carry)
    return sum_list


if __name__ == '__main__':
    list1 = List([9, 9, 9, 9])
    list2 = List([0, 1, 1])
    sum_list = add(list1, list2)

    print('{} + {} = {}'.format(list1, list2, sum_list))
