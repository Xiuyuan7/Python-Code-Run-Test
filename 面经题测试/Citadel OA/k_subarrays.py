class Solution:
    """
    @params: nums:List[int], k:int
    @return: int
    @Time: O(N)
    @Space: O(N)
    """
    def k_subarrays(self, nums, k):
        result = 0
        # A dictionary recording prefix_sum % k and count
        module_to_count = {0: 1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            module = prefix_sum % k

            # If sum of 0 to i module k equals sum of 0 to j module k, then sum of i to j is divisible by k
            if module in module_to_count:
                result += module_to_count[module]
                module_to_count[module] += 1
            else:
                module_to_count[module] = 1

        return result


s = Solution()

nums = [4, 5, 0, -2, -3, 1]
k = 5
print(s.k_subarrays(nums, k))  # 7

nums = [5]
k = 9
print(s.k_subarrays(nums, k))  # 0
