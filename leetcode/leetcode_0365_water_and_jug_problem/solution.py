SEEN = -1


def can_measure(x, y, target, cache, xvol=0, yvol=0):
    try:
        res = cache[x, y, target, xvol, yvol]
        if res == SEEN:
            return False
        return res
    except KeyError:
        cache[x, y, target, xvol, yvol] = SEEN

    # if x + y < target:
    # cache[x, y, target, xvol, yvol] = False
    # return False
    if xvol == target or yvol == target or (xvol + yvol) == target:
        cache[x, y, target, xvol, yvol] = True
        return cache[x, y, target, xvol, yvol]

    # Path 1: fill x
    if xvol < x and can_measure(x, y, target, cache, x, yvol):
        cache[x, y, target, x, yvol] = True
        return True

    # Path 2: fill y
    if yvol < y and can_measure(x, y, target, cache, xvol, y):
        cache[x, y, target, xvol, y] = True
        return True

    # Path 3: empty x
    if xvol > 0 and can_measure(x, y, target, cache, 0, yvol):
        cache[x, y, target, 0, yvol] = True
        return True

    # Path 4: empty y
    if yvol > 0 and can_measure(x, y, target, cache, xvol, 0):
        cache[x, y, target, xvol, 0] = True
        return True

    # Path 5: transfer x -> y
    if xvol > 0 and yvol < y:
        amount = min(xvol, y - yvol)
        if can_measure(x, y, target, cache, xvol - amount, yvol + amount):
            cache[x, y, target, xvol - amount, yvol + amount] = True
            return True

    # Path 6: transfer y -> x
    if yvol > 0 and xvol < x:
        amount = min(yvol, x - xvol)
        if can_measure(x, y, target, cache, xvol + amount, yvol - amount):
            cache[x, y, target, xvol + amount, yvol - amount] = True
            return True

    # All paths exhausted
    cache[x, y, target, xvol, yvol] = False
    return False


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # if (x, y, target) == (3, 5, 4):
        # breakpoint()
        return can_measure(x, y, target, {})
