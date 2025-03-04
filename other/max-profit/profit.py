"""
For a given stock, we are given a list of stock prices that increment
every minute. For example:

Prices(p): [4, 5, 9, 5, 3, 9, 2, 6]

Determine the biggest profit you can make through one buy and one sell

Solution: Buy at t=4, Sell at t=5, Profit = t(5) - t(4) = 9 - 3 = 6
"""

import logging


def calculate_max_profit(prices: list[int]) -> int:
    logging.debug(f"{prices=}")
    prices = iter(prices)
    max_profit = 0
    smallest = previous_price = next(prices)
    logging.debug(f"{smallest=}, {previous_price=}, {max_profit=}")
    for price in prices:
        max_profit = max(price - smallest, max_profit)
        logging.debug(f"{price=}, {smallest=}, {previous_price=}, {max_profit=}")
        if price - previous_price < 0:
            logging.debug(f"    {price=} is smaller than {previous_price=}")
            smallest = min(smallest, price)
            logging.debug(f"    Update {smallest=}")

    return max_profit
