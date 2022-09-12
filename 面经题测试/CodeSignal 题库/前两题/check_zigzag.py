def solution(nums):
    result = []

    for i in range(2, len(nums)):
        left, mid, right = nums[i - 2], nums[i - 1], nums[i]
        if mid > left and mid > right or mid < left and mid < right:
            result.append(1)
        else:
            result.append(0)

    return result


nums = [1, 2, 1, 3, 4]
print(solution(nums))
