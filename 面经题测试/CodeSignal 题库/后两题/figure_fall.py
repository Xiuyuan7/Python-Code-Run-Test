class Solution:
    def figure_fall(self, field, figure):
        rows, cols = len(field), len(field[0])
        # print(rows, cols)

        for col in range(cols - 2):
            for row in range(rows - 2):
                # print(self.is_blocked(field, figure, row, col))
                if self.is_blocked(field, figure, row, col):
                    # print(self.find_occupied_row(field, figure, row, col))
                    if self.find_occupied_row(field, figure, row, col):
                        return col
                    break

        return -1


    def is_blocked(self, field, figure, row, col):
        # print(row)
        for j in range(3):
            for i in range(2, -1, -1):
                # print(i, j, figure[i][j])
                if figure[i][j] == 1:
                    # print(row + i == len(field) - 1)
                    if row + i == len(field) - 1 or field[row + i + 1][col + j] == 1:
                        return True
                    break

        return False


    def find_occupied_row(self, field, figure, row, col):
        rows, cols = len(field), len(field[0])

        for i in range(rows - 1, -1, -1):
            for j in range(cols):
                # print(i, j)
                if row <= i < row + 3 and col <= j < col + 3:
                    if field[i][j] == 0 and figure[i - row][j - col] == 0:
                        break
                else:
                    if field[i][j] == 0:
                        break
            else:
                return True

        return False


solu = Solution()

field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
]

figure = [
    [0, 0, 1],
    [0, 1, 1],
    [0, 0, 1]
]

print(solu.figure_fall(field, figure))

field = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

figure = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
]

print(solu.figure_fall(field, figure))

field = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 1]
]

figure = [
    [1, 1, 0],
    [1, 0, 0],
    [1, 0, 0]
]

print(solu.figure_fall(field, figure))
