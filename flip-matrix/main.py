def flippingMatrix(matrix):
    size = len(matrix)
    half = size // 2

    max_sum = 0
    for row in range(half):
        for col in range(half):
            max_sum += max(
                matrix[row][col],
                matrix[row][size - col - 1],
                matrix[size - row - 1][col],
                matrix[size - row - 1][size - col - 1],
            )
    return max_sum
