from typing import List


def collision_test(a1, a2):
    if not (a1 >= 0 and a2 < 0):
        return "no collision"
    if abs(a1) > abs(a2):
        return "kill right"
    elif abs(a1) < abs(a2):
        return "kill left"
    else:
        return "kill both"


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        out = []
        for asteroid in asteroids:
            if not out or collision_test(out[-1], asteroid) == "no collision":
                out.append(asteroid)
                continue

            while out and collision_test(out[-1], asteroid) == "kill left":
                del out[-1]

            if not out or collision_test(out[-1], asteroid) == "no collision":
                out.append(asteroid)
            elif collision_test(out[-1], asteroid) == "kill both":
                del out[-1]
            # In case of 'kill right', we do not need to do anything

        return out
