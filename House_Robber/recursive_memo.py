# here we do the same approach but with use mmeoization to store values
# this works in O(n) time but the space usage is O(n) as well


def house_robber_recursive(nums):
    # set up mem count_sub_array
    mem = [-1] * len(nums)
    return recur(nums, len(nums)-1, mem)


def recur(nums, i, mem):
    if i < 0:
        return 0
    elif mem[i] >= 0:
        return mem[i]
    result = max(recur(nums, i-2, mem) + nums[i], recur(nums, i-1, mem))
    mem[i] = result
    return result


res = house_robber_recursive([2, 1, 9, 15, 7])
print(res)
