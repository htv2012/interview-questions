import collections


def lonelyinteger(a):
    counter = collections.defaultdict(int)
    for value in a:
        counter[value] += 1
    return next((k for k, v in counter.items() if v == 1), "not found")
