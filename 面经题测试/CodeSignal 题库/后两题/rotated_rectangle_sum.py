class Solution:
    def rectangle_sum(self, matrix, a, b):
        rows, cols = len(matrix), len(matrix[0])
        # print(rows, cols)
        max_sum = float("-inf")
        side = a + b - 1
        # print(side)

        for row in range(0, rows - side + 1):
            for col in range(0, cols - side + 1):
                cur_sum = self.get_sum(matrix, a, b, row, col)
                # print(cur_sum)
                if cur_sum > max_sum:
                    max_sum = cur_sum
                cur_sum = self.get_sum(matrix, b, a, row, col)
                if cur_sum > max_sum:
                    max_sum = cur_sum

        return max_sum if max_sum != float("-inf") else -1

    def get_sum(self, matrix, a, b, row, col):
        side = a + b - 1

        total_sum = 0
        for i in range(row, row + side):
            for j in range(col, col + side):
                total_sum += matrix[i][j]

        top_left_sum, bottom_right_sum = 0, 0
        for i in range(side - b):
            for j in range(side - b - i):
                # 左下至右上斜脚线对称的坐标关系
                top_left_sum += matrix[row + i][col + j]
                bottom_right_sum += matrix[row + side - j - 1][col + side - i - 1]

        top_right_sum, bottom_left_sum = 0, 0
        for i in range(a, side):
            for j in range(i - a + 1):
                # 左上至右下斜脚线对称的坐标关系
                top_right_sum += matrix[row + i][col + j]
                bottom_left_sum += matrix[col + j][row + i]

        return total_sum - top_right_sum - top_left_sum - bottom_left_sum - bottom_right_sum


s = Solution()

matrix = [
    [1, 2, 3, 4, 0],
    [5, 6, 7, 8, 1],
    [3, 2, 4, 1, 4],
    [4, 3, 5, 1, 6]
]
a, b = 2, 3
print(s.rectangle_sum(matrix, a, b))

matrix = [
    [-2, 3, 5, -1],
    [4, 3, -10, 10]
]
a, b = 1, 1
print(s.rectangle_sum(matrix, a, b))

matrix = [
    [-2, 3],
    [4, 3]
]
a, b = 1, 2
print(s.rectangle_sum(matrix, a, b))
