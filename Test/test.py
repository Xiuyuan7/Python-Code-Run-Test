class UnionFind:
    def __init__(self, n):
        self.parents = [-1]
        self.size = n
        self.szList = [-1]
        for i in range(n):
            self.parents.append(i + 1)
            self.szList.append(1)
        print(self.parents)
        print(self.szList)

    def union(self, a, b):
        root_a = self.get_root(a)
        root_b = self.get_root(b)

        if root_a != root_b:
            if self.szList[root_a] < self.szList[root_b]:
                self.szList[root_b] += self.szList[root_a]
                self.parents[root_a] = root_b
            else:
                self.szList[root_a] += self.szList[root_b]
                self.parents[root_b] = root_a

    # No consideration: a and b are in same group
    # def getTotal(self, a, b):
    #     return self.szList[self.find(a)]+ self.szList[self.find(b)]

    def get_root(self, k):
        if self.parents[k] == k:
            return k
        return self.get_root(self.parents[k])

    def get_total(self, a, b):
        x = self.get_root(a)
        y = self.get_root(b)
        if x != y:
            return self.szList[x] + self.szList[y]
        else:
            return self.szList[x]


class Solution:
    def get_the_groups(self, n, queries, students1, students2):
        students = UnionFind(n)
        result = []
        for i in range(len(queries)):
            if queries[i] == "Friend":
                students.union(students1[i], students2[i])
            else:
                result.append(students.get_total(students1[i], students2[i]))

        return result


s = Solution()

n = 4
queryType = ["Friend", "Friend", "Total"]
student1 = [1, 2, 1]
student2 = [2, 3, 4]
print(s.get_the_groups(n, queryType, student1, student2))  # [4]
