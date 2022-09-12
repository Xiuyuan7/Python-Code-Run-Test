def solution(s):
    count = 0

    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            a = s[:i]
            b = s[i:j]
            c = s[j:]

            if a + b != b + c and b + c != c + a and c + a != a + b:
                count += 1

    return count


s = "xzxzx"
print(solution(s))
