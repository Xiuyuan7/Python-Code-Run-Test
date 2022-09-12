def solution(board):
    row_cnt = len(board)
    col_cnt = len(board[0])
    lowest_row = get_lowest_row(board)
    falling_distance = row_cnt - lowest_row - 1

    min_removed = 0
    for row in range(row_cnt):
        for col in range(col_cnt):
            if board[row][col] == '*':
                for i in range(1, falling_distance + 1):
                    if board[row + i][col] == '#':
                        min_removed += 1
                    elif board[row + i][col] == '*':
                        break
    return min_removed


def get_lowest_row(board):
    row_cnt = len(board)
    col_cnt = len(board[0])
    for row in range(row_cnt - 1, -1, -1):
        for col in range(col_cnt):
            if board[row][col] == '*':
                return row
    return -1


board = [
    ['*', '*', '*'],
    ['#', '*', '*'],
    ['*', '*', '-'],
    ['-', '-', '-'],
    ['-', '#', '#']
]
print(solution(board))  # 2

print('------')

board = [
    ['_', '*', '_'],
    ['*', '*', '*'],
    ['_', '*', '_'],
    ['#', '#', '#'],
    ['#', '#', '#']
]
print(solution(board))  # 4
