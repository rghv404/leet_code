def max_product_subarray(nums):
    curr_max = curr_min = ans = nums[0]
    for num in nums[1:]:
        curr_min, curr_max = min(num, curr_min*num, curr_max *
                                 num), max(num, curr_min*num, curr_max*num)
        ans = max(ans, curr_max)
    return ans


res = max_product_subarray([-2, -3, -4, -6])
print(res)
