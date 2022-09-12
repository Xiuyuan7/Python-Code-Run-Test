# Difference array
class Solution:
    """
    @params: sprints:List[int], n:int
    @return: int
    @Time: O(N)
    @Space: O(N)
    """
    def sprint_training(self, sprints,  n):
        # Index is marker number and value is the number of visits
        markers = [0] * (n + 1)
        difference_array = [0] * (n + 2)

        # Update difference array for each sprint
        for i in range(len(sprints) - 1):
            start = min(sprints[i], sprints[i + 1])
            end = max(sprints[i], sprints[i + 1])
            difference_array[start] += 1
            difference_array[end + 1] -= 1

        print(difference_array)
        result = 0

        # Use difference array to update markers after all sprints and record the index of maximum val
        for i in range(1, n + 1):
            if i == 1:
                markers[i] = difference_array[i]
            else:
                markers[i] = difference_array[i] + markers[i - 1]

            if markers[i] > markers[i - 1]:
                result = i

        print(markers)

        return result


s = Solution()

sprints = [2, 4, 1, 3]
n = 5
print(s.sprint_training(sprints, n))  # 2
