class Solution:
    def count_times(self, nums):
        counter = [0 for _ in range(10)]
        result = []

        for num in nums:
            while num > 0:
                digit = num % 10
                num //= 10
                counter[digit] += 1

        max_times = max(counter)

        for num, times in enumerate(counter):
            if times == max_times:
                result.append(num)

        return result


solu = Solution()

nums = [25, 2, 3, 57, 38, 41]
print(solu.count_times(nums))
