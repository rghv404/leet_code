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
