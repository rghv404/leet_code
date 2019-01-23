# the problem is of maximizing the sum of positive integer matrix but you can'#
# select the neighboring item


def house_robber_recursive(nums):
    # the idea is simple for any element (bottome up) either we select it or not
    # if we select it then we add max_sum upto that house and current index's max_val
    # if not we go to house i-1 and repeat
    return recur(nums, len(nums)-1)


def recur(nums, i):
    if i < 0:
        return 0
    # max of selecting this house plus curr value or prev house
    return max(recur(nums, i-2) + nums[i], recur(nums, i-1))


# this solution takes o_n2 time due to same house value calculated multiple times
res = house_robber_recursive([2, 1, 9, 15, 7])
print(res)
