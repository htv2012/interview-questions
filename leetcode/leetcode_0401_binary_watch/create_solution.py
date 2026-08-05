import collections
import pathlib

solution = """
from typing import List

hours = %r


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return hours.get(turnedOn, [])

"""


def count_1(n: int):
    count = 0
    while n > 0:
        n, one = divmod(n, 2)
        count += one
    return count


def main():
    ones_count = {n: count_1(n) for n in range(60)}
    counter = collections.defaultdict(list)

    for hour in range(12):
        for minute in range(60):
            total = ones_count[hour] + ones_count[minute]
            counter[total].append(f"{hour}:{minute:>02}")

    hours = {k: sorted(v) for k, v in counter.items()}
    pathlib.Path("solution.py").write_text(solution % hours)


if __name__ == "__main__":
    main()
