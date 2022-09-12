def solution(arr):
    rows = len(arr)
    cols = 0
    result = []

    for s in arr:
        cols = max(cols, len(s))

    for j in range(cols):
        for i in range(rows):
            if j > len(arr[i]) - 1:
                continue
            result.append(arr[i][j])

    return "".join(result)


arr = ["Daisy", "Rose", "Hyacinth", "Poppy"]
print(solution(arr))

arr = ["E", "M", "I", "L", "Y"]
print(solution(arr))
