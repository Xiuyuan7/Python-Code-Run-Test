class Solution:
    """
    @params: n:int, queries:List[str], students1:List[int], students2:List[int]
    @return: List[int]
    @Time: O(KlogN)
    @Space: O(N)
    """
    def get_the_groups(self, n, queries, students1, students2):
        students = UnionFind(n)
        result = []

        for i in range(len(queries)):
            if queries[i] == "Friend":
                students.union(students1[i], students2[i])
            else:
                result.append(students.get_total(students1[i], students2[i]))

        return result


class UnionFind:
    def __init__(self, n):
        self.parents = [-1] + [i + 1 for i in range(n)]
        self.sizes = [-1] + [1 for _ in range(n)]
        print(self.parents)
        print(self.sizes)

    def union(self, a, b):
        root_a = self.get_root(a)
        root_b = self.get_root(b)

        if root_a != root_b:
            if self.sizes[root_a] < self.sizes[root_b]:
                self.sizes[root_b] += self.sizes[root_a]
                self.parents[root_a] = root_b
            else:
                self.sizes[root_a] += self.sizes[root_b]
                self.parents[root_b] = root_a

    def get_root(self, k):
        if self.parents[k] == k:
            return k
        return self.get_root(self.parents[k])

    def get_total(self, a, b):
        root_a = self.get_root(a)
        root_b = self.get_root(b)
        if root_a != root_b:
            return self.sizes[root_a] + self.sizes[root_b]
        else:
            return self.sizes[root_a]


s = Solution()

n = 4
queries = ['Friend', 'Friend', 'Total']
students1 = [1, 2, 1]
students2 = [2, 3, 4]
print(s.get_the_groups(n, queries, students1, students2))  # [4]

n = 3
queries = ['Friend', 'Total']
students1 = [1, 2]
students2 = [2, 3]
print(s.get_the_groups(n, queries, students1, students2))  # [3]

n = 2
queries = ['Total']
students1 = [1]
students2 = [2]
print(s.get_the_groups(n, queries, students1, students2))  # [2]
