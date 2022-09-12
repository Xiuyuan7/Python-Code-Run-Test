"""
@Time: O(MN)
@Space: O(MN)
"""
from collections import deque

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1,), (1, 0), (1, 1)]


def solution(field, x, y):
    rows, cols = len(field), len(field[0])
    results = [[-1] * cols for _ in range(rows)]
    queue = deque()
    visited = set()

    results[x][y] = count_mines(field, x, y)

    if results[x][y] == 0:
        queue.append((x, y))
        visited.add((x, y))

    while queue:
        i, j = queue.popleft()
        for di, dj in DIRECTIONS:
            new_i, new_j = i + di, j + dj
            if not (0 <= new_i < rows) or not (0 <= new_j < cols):
                continue
            mines = count_mines(field, new_i, new_j)
            results[new_i][new_j] = mines
            if mines == 0 and (new_i, new_j) not in visited:
                queue.append((new_i, new_j))
                visited.add((new_i, new_j))

    return results


def count_mines(field, i, j):
    rows, cols = len(field), len(field[0])
    count = 0

    for di, dj in DIRECTIONS:
        new_i, new_j = i + di, j + dj
        if not (0 <= new_i < rows) or not (0 <= new_j < cols):
            continue

        if field[new_i][new_j]:
            count += 1

    return count


field = [
    [False, True, True],
    [True, False, True],
    [False, False, True],
]
x, y = 1, 1
print(solution(field, x, y))
