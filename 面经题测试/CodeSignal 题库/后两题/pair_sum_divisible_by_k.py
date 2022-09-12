

"""
@Time: O(N + K)
"""
def solution(a, k):
    result = 0
    freqs = [0] * k

    for n in a:
        freqs[n % k] += 1

    print(freqs)

    result += freqs[0] * (freqs[0] - 1) / 2

    # if k % 2 == 0:
    #     for i in range(1, k // 2):
    #         result += freqs[i] * freqs[k - i]
    #     result += freqs[k // 2] * (freqs[k // 2] - 1) / 2
    # else:
    #     for i in range(1, k // 2 + 1):
    #         result += freqs[i] * freqs[k - i]

    for i in range(1, (k + 1) // 2):
        result += freqs[i] * freqs[k - i]

    if k % 2 == 0:
        result += freqs[k // 2] * (freqs[k // 2] - 1) / 2

    return result


a = [1, 2, 3, 4, 5]
k = 3
print(solution(a, k))

a = [1, 3, 5, 7, 9]
k = 2
print(solution(a, k))
