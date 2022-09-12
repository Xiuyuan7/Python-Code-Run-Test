class Solution:
    def sudoku_check(self, grid):
        for row in range(9):
            visited = set()
            for col in range(9):
                if grid[row][col] in visited:
                    return False
                visited.add(grid[row][col])

        for col in range(9):
            visited = set()
            for row in range(9):
                if grid[row][col] in visited:
                    return False
                visited.add(grid[row][col])

        for i in range(0, 3, 6):
            for j in range(0, 3, 6):
                visited = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if grid[row][col] in visited:
                            return False
                        visited.add(grid[row][col])

        return True


def main():
    grid = [
        [1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]
    ]
    s = Solution()
    print(s.sudoku_check(grid))


main()
