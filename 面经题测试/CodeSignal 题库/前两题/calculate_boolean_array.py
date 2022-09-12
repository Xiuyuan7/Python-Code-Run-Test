class Solution:
    def calculate_boolean_array(self, nums, left, right):
        result = []

        for i, num in enumerate(nums):
            x = num // (i + 1)
            if x * (i + 1) != num:
                result.append(False)
            else:
                if left <= x <= right:
                    result.append(True)
                else:
                    result.append(False)

        return result


s = Solution()

nums = [8, 5, 6, 16, 5]
left, right = 1, 3
print(s.calculate_boolean_array(nums, left, right))
        