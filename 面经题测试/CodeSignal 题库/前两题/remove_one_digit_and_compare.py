class Solution:
    """
    @Time: O(M + N)
    """
    def count_ways(self, s, t):
        count = 0

        for i, char in enumerate(s):
            if not char.isdigit():
                continue
            new_s = s[:i] + s[i + 1:]
            if new_s < t:
                count += 1

        for i, char in enumerate(t):
            if not char.isdigit():
                continue
            new_t = t[:i] + t[i + 1:]
            if s < new_t:
                count += 1

        return count


solu = Solution()

s = "ab12c"
t = "1zz456"
print(solu.count_ways(s, t))

s = "ab12c"
t = "ab24z"
print(solu.count_ways(s, t))
