#!/usr/bin/env python3
"""
Problem:
Given a menu such as:

AB, 1.75
AC, 2.05
BD, 3.10

Where each item is unique and the price is also unique. Also given
a budget of $15.05, write a function which takes in the menu and
the budget and returns True if we can buy items from the menu using
the budget and there is not a cent over or under budget.
"""
from decimal import Decimal


def fits_budget(menu: list, budget: float):
    # menu = [(name, Decimal(price)) for name, price in menu]
    # budget = Decimal(budget)
    menu = menu.copy()

    if not menu:
        return False

    if len(menu) == 1:
        _, price = menu[0]
        return budget % price == 0

    # Multiple items, pop one of them
    _, unit_price = menu.pop()
    iterations = int(budget // unit_price)

    for trial in range(iterations + 1):
        remaining = budget - trial * unit_price
        fitted = fits_budget(menu, remaining)
        if fitted:
            return True

    return False


def test_empty_menu():
    assert fits_budget([], Decimal("15.0")) is False


def test_one_item_expect_true():
    assert fits_budget([("ab", Decimal("5.01"))], Decimal("5.01")) is True
    assert fits_budget([("ab", Decimal("5.01"))], Decimal("10.02")) is True
    assert fits_budget([("ab", Decimal("5.01"))], Decimal("15.03")) is True


def test_one_item_expect_false():
    assert fits_budget([("ab", Decimal("5.01"))], Decimal("5.02")) is False


def test_one_item_expect_false_multiple_times():
    assert fits_budget([("ab", Decimal("5.01"))], Decimal("10.03")) is False


def test_two_items_expect_true():
    menu = [("item1", Decimal("5.01")), ("item2", Decimal("3.72"))]
    assert fits_budget(menu, Decimal("8.73")) is True


def test_two_items_expect_true_multiple():
    menu = [("item1", Decimal("5.01")), ("item2", Decimal("3.72"))]
    assert fits_budget(menu, Decimal("22.47")) is True


def test_two_items_expect_false():
    menu = [("item1", Decimal("5.01")), ("item2", Decimal("3.72"))]
    assert fits_budget(menu, budget=Decimal("5.02")) is False


def test_three_items_expect_true():
    menu = [
        ("item1", Decimal("5.01")),
        ("item2", Decimal("3.72")),
        ("item3", Decimal("2.37")),
    ]
    assert fits_budget(menu, budget=Decimal("11.10")) is True


def test_three_items_expect_true_multiple():
    menu = [
        ("item1", Decimal("5.01")),
        ("item2", Decimal("3.72")),
        ("item3", Decimal("2.37")),
    ]
    budget = Decimal("41.76")  # 5.01*3 + 3.72*4 + 2.37*5
    assert fits_budget(menu, budget) is True
