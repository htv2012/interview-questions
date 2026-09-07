class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == 1:
            return 1

        pillow = 1  # initial pillow position
        direction = 1

        for _ in range(time):
            # advance and change direction at the two ends
            pillow += direction
            if pillow == n or pillow == 1:
                direction *= -1
        return pillow
