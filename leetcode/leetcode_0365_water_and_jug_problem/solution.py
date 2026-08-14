SEEN = -1


def can_measure(x, y, target, cache, xvol=0, yvol=0):
    key = (x, y, target, xvol, yvol)
    try:
        res = cache[key]
        if res == SEEN:
            return
        return res
    except KeyError:
        cache[key] = SEEN

    if x + y < target:
        cache[key] = False
        return False
    elif x + y == target:
        cache[key] = True
        return cache[key]

    # Path 1: fill x
    if xvol < x:
        print()
        if can_measure(x, y, target, cache, x, yvol):
            cache[key] = True
            return cache[key]

    # Path 2: fill y
    if yvol < y:
        print()
        if can_measure(x, y, target, cache, xvol, y):
            cache[key] = True
            return cache[key]

    # Path 3: empty x
    if xvol > 0:
        print()
        if can_measure(x, y, target, cache, 0, yvol):
            cache[key] = True
            return cache[key]

    # Path 4: empty y
    if yvol > 0:
        print()
        if can_measure(x, y, target, cache, xvol, 0):
            cache[key] = True
            return cache[key]

    # Path 5: transfer x -> y
    if xvol > 0 and yvol < y:
        amount = min(xvol, y - yvol)
        if can_measure(x, y, target, cache, xvol - amount, yvol + amount):
            cache[key] = True
            return cache[key]

    # Path 6: transfer y -> x
    if yvol > 0 and xvol < x:
        amount = min(yvol, x - xvol)
        if can_measure(x, y, target, cache, xvol + amount, yvol - amount):
            cache[key] = True
            return cache[key]

    # All paths exhausted
    cache[key] = False
    return cache[key]


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return can_measure(x, y, target, {})
