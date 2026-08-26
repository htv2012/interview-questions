from decimal import Decimal, getcontext


def plusMinus(arr):
    pos, zero, neg = 0, 0, 0
    count = len(arr)
    for value in arr:
        if value > 0:
            pos += 1
        elif value < 0:
            neg += 1
        else:
            zero += 1

    getcontext().prec = 6
    for num in [pos, neg, zero]:
        ratio = Decimal(num) / Decimal(count)
        print(f"{ratio:0.6f}")
