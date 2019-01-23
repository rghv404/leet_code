# striclt less than k
def count_sub_arrays(lst, k):
    if k <= 1:
        return 0
    left, count = 0, 0
    prod = 1
    for right, val in enumerate(lst):
        # here we calculate the product up until right end
        prod *= val
        # now we check if the prod till right end is less than k or note
        # if it is not then we remove the left most val freom teh prod and
        # increment left until the product is less than k
        while prod >= k:
            prod /= lst[left]
            left += 1
        # if the product is stricly less than we add to ans all elements b/w
        # right and left and 1 for combination of it
        count += right - left + 1
    return count


# less than equal to k
def count_sub_arrays_less_than_equal(lst, k):
    if k < 1:
        return 0
    left, count = 0, 0
    prod = 1
    d_ = dict()
    for right, val in enumerate(lst):
        # here we calculate the product up until right end
        prod *= val
        # now we check if the prod till right end is less than k or note
        # if it is not then we remove the left most val from the prod and
        # increment left until the product is less than k
        while prod > k:
            prod /= lst[left]
            left += 1
        # if the product is stricly less than we add to ans all elements b/w
        # right and left and 1 for combination of it
    return count


ans = count_sub_arrays([1, 1, 1], 1)
print(ans)
ans = count_sub_arrays_less_than_equal([1, 1, 1], 1)
ans = count_sub_arrays_less_than_equal([5, 2, 2, 5], 10)
print(ans)
