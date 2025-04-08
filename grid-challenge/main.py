def gridChallenge(grid):
    grid = [sorted(row) for row in grid]
    for col in zip(*grid):
        if sorted(col) != list(col):
            return "NO"
    return "YES"
