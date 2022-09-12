class Solution:
    """
    @Time: O(N)
    """
    def array_mutation(self, nums):
        result = []

        for i in range(len(nums)):
            if i == 0:
                pre = 0
            else:
                pre = nums[i - 1]

            cur = nums[i]

            if i == len(nums) - 1:
                post = 0
            else:
                post = nums[i + 1]

            result.append(pre + cur + post)

        return result


s = Solution()

nums = [4, 0, 1, -2, 3]
print(s.array_mutation(nums))
