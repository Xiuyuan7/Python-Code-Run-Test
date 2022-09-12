# Sliding window technique
class Solution:
    """
    @params: nums:List[int], k:int
    @return: int
    @Time: O(N)
    @Space: O(1)
    """
    def maxLength(self, nums, k):
        sum_ = 0
        count = 0
        max_count = 0

        for i in range(len(nums)):
            # If adding current number doesn't exceed the limit k, add it to current window
            if sum_ + nums[i] <= k:
                sum_ += nums[i]
                count += 1
            # Else, delete the first number of current window and add current number
            else:
                sum_ = sum_ - nums[i - count] + nums[i]

            # Record occurred maximum length
            max_count = max(max_count, count)

        return max_count


s = Solution()

nums = [1, 2, 1, 0, 1, 1, 0]
k = 4
print(s.maxLength(nums, k))  # 5

nums = [1, 2, 3]
k = 3
print(s.maxLength(nums, k))  # 2
