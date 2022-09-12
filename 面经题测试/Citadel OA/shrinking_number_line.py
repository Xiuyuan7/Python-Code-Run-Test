class Solution:
    """
    @params: nums:List[int], k:int
    @return: int
    @Time: O(NlogN)
    @Space: O(1)
    """
    def shrinking_number_line(self, nums, k):
        nums.sort()
        min_val, max_val = nums[0], nums[-1]
        # The smallest difference must equal to or less than the difference of maximum value and minimum value
        result = max_val - min_val

        # Enumerate every two adjacent numbers to update the minimum value of the result
        for i in range(len(nums) - 1):
            num1, num2 = nums[i], nums[i + 1]
            # Record the smallest value from the difference
            result = min(result, max(max_val - k, num1 + k) - min(min_val + k, num2 - k))

        return result


s = Solution()

nums = [0, 1, 2, 3]
k = 2
print(s.shrinking_number_line(nums, k))  # 3

nums = [-3, 0, 1]
k = 3
print(s.shrinking_number_line(nums, k))  # 3

nums = [4, 7, -7]
k = 5
print(s.shrinking_number_line(nums, k))  # 4

nums = [-100000, 100000]
k = 100000
print(s.shrinking_number_line(nums, k))  # 0
