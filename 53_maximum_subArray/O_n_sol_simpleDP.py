def maximum_subarray(lst):
    if lst is None:
        return
    if len(lst) == 1:
        return lst[0]
    max_at_i = [lst[-1]]
    max_val = max_at_i[-1]
    r = len(lst) - 2
    while r >= 0:
        max_at_i.append(max(max_at_i[-1] + lst[r], lst[r]))
        max_val = max(max_val, max_at_i[-1])
        r -= 1
    return max_val


lst = [15, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = maximum_subarray(lst)
print(max_sum)

# O_N time and O_1 space KADANE's algo


def max_sum_subArray(nums):
    if nums is None:
        return
    ans = max_sum = nums[0]
    for num in nums[1:]:
        max_sum = max(max_sum+num, num)
        ans = max(ans, max_sum)
    return ans


res = max_sum_subArray([15, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
