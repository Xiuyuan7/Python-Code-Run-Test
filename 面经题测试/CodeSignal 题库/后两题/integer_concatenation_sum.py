class Solution:
    """
    @Time: O(N)
    """
    def concatenation_sum(self, nums):
        result = 0
        factor = 0

        for num in nums:
            factor += 10 ** (len(str(num)))

        for num in nums:
            result += num * factor
            result += num * len(nums)

        return result


solu = Solution()

nums = [10, 2]
print(solu.concatenation_sum(nums))

nums = [8]
print(solu.concatenation_sum(nums))

nums = [1, 2, 3]
print(solu.concatenation_sum(nums))
