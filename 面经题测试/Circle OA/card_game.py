from collections import deque


class Solution:
    def card_game(self, deck1, deck2):
        queue1 = deque(deck1)
        queue2 = deque(deck2)
        count = 0

        while queue1 and queue2:
            num1 = queue1.popleft()
            num2 = queue2.popleft()
            count += 1
            if num1 >= num2:
                queue1.append(num1)
                queue1.append(num2)
            else:
                queue2.append(num2)
                queue2.append(num1)

        return count


s = Solution()

deck1 = [5]
deck2 = [2]
print(s.card_game(deck1, deck2))

deck1 = [1, 2]
deck2 = [3, 1]
print(s.card_game(deck1, deck2))
