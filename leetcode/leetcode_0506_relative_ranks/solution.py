from typing import List


def find_relative_ranks(score: List[int]) -> List[str]:
    # rank is a list of (score, index, ranking), ordered by score
    rank = sorted([[e, i, ""] for i, e in enumerate(score)], reverse=True)

    for i, t in enumerate(rank, 1):
        t[2] = str(i)
    try:
        rank[0][2] = "Gold Medal"
        rank[1][2] = "Silver Medal"
        rank[2][2] = "Bronze Medal"
    except IndexError:
        pass

    # Order by indices and extract the ranking
    rank.sort(key=lambda t: t[1])
    return [t[2] for t in rank]


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        return find_relative_ranks(score)
