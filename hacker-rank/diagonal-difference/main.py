def diagonalDifference(arr):
    return abs(sum(row[i] - row[-i - 1] for i, row in enumerate(arr)))
