from math import sqrt
from collections import deque


class Solution:
    """
    @params: c:int, x1:int, y1:int, x2:int, y2:int
    @return: str
    """
    def can_reach(self, c, x1, y1, x2, y2):
        if self.is_obstacle(x1, y1):
            return 'No'
        if self.is_obstacle(x2, y2):
            return 'No'
        if (x1, y1) == (x2, y2):
            return 'Yes'

        queue = deque([(x1, y1)])
        # the literal construction is faster
        visited = {(x1, y1)}

        while queue:
            x, y = queue.popleft()
            for next_x, next_y in [(x, x + y), (x + y, y), (x + c, y + c)]:
                if self.is_obstacle(next_x, next_y):
                    continue
                if not (0 <= next_x <= x2) or not (0 <= next_y <= y2):
                    continue
                if (next_x, next_y) in visited:
                    continue
                if (next_x, next_y) == (x2, y2):
                    return 'Yes'
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

        return 'No'

    """
    @params: x:int, y:int
    @return: bool
    """
    def is_obstacle(self, x, y):
        sum_ = x + y
        root = sqrt(sum_)
        if int(root) ** 2 == sum_:
            return True
        return False


s = Solution()
c = 1
x1, y1 = 1, 4
x2, y2 = 7, 6
print(s.can_reach(c, x1, y1, x2, y2))
