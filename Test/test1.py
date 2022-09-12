from collections import deque


def solution(field, x, y):
    rows, cols = len(field), len(field[0])
    results = [[-1] * cols for _ in range(rows)]
    print(results)
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        results[x][y] = count_mines(field, x, y)
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, -1)]:
            next_x, next_y = x + dx, y + dy
            if not (0 <= next_x < rows) or not (0 <= next_y < cols):
                continue

            count = count_mines(field, next_x, next_y)
            results[next_x][next_y] = count
            if count == 0:
                queue.append((next_x, next_y))

    print(results)
    return results


def count_mines(field, x, y):
    count = 0
    rows, cols = len(field), len(field[0])
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, -1)]:
        next_x, next_y = x + dx, y + dy
        if not (0 <= next_x < rows) or not (0 <= next_y < cols):
            continue
        if field[next_x][next_y]:
            count += 1

    return count


def main():
    field = [[False, True, True],
             [True, False, True],
             [False, False, True]]
    print(solution(field, 1, 1))


main()