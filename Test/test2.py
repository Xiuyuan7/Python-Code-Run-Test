def get_sum(matrix, a, b, row, col):
    side = a + b - 1

    total_sum = 0
    for i in range(row, row + side):
        for j in range(col, col + side):
            total_sum += matrix[i][j]
    print(total_sum)

    top_left_sum, bottom_right_sum = 0, 0
    for i in range(side - b):
        for j in range(side - b - i):
            print(matrix[row + i][col + j])
            top_left_sum += matrix[row + i][col + j]
            print(matrix[row + side - j - 1][col + side - i - 1])
            bottom_right_sum += matrix[row + side - j - 1][col + side - i - 1]

    top_right_sum, bottom_left_sum = 0, 0
    for i in range(a, side):
        for j in range(i - a + 1):
            print(matrix[row + i][col + j])
            top_right_sum += matrix[row + i][col + j]
            print(matrix[col + j][row + i])
            bottom_left_sum += matrix[col + j][row + i]

    return total_sum - top_right_sum - top_left_sum - bottom_left_sum - bottom_right_sum


matrix = [
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41, 42, 43, 44, 45],
    [50, 51, 52, 53, 54, 55],
    [60, 61, 62, 63, 64, 65]
]
a, b = 3, 4
row, col = 0, 0
print(get_sum(matrix, a, b, row, col))
print()
print(get_sum(matrix, b, a, row, col))
