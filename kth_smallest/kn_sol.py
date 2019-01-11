def get_ordered_k_element(lst, k):
    for i in range(k):
        min_index = i
        min_val = lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] < min_val:
                min_index = j
                min_val = lst[j]
                # swap the two values
                lst[i], lst[min_index] = min_val, lst[i]
    print(lst)
    return lst[k-1]


# above method was partial selection sort with O(kn) time
# second method is using the quick select in O(n) time average case
# quick select, w're beasically dividing the array from a pivot index  such that
# left side, all are smaller and right side all elements are bigger, depedign on the index we're trying to find
# we then do the same process for left or right side of the array ultimatrely landing on teh desired index
# since we're only partitioning one side of the array with each iteration the average running time is O(n) rather than O(nlogn)

def select (lst, left, right, k):
    pivot_i = (left + right + 1) // 2
    pivot_val = lst[pivot_i]
    # move pivot to right end of the list
    lst[right], lst[pivot_i] = lst[pivot_i], lst[right]
    # partition array by pivot
    i = left
    for j in range(left, right):
        if lst[j] < pivot_val:
            # swap the ith and jth element
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    # swap th epivot to ith position, this operation will render left and right of pivot smaller and larger respectively
    lst[right], lst[i] = lst[i], lst[right]
    # now we recurively call the select function on the side where k is
    if i == k-1:
        print('IS it not equal')
        print(lst[i])
        return lst[i]
    elif i > k - 1:
        # run select on left side
        return select(lst,left, i-1, k)
    else:
        return select(lst,i+1, right, k)


item = get_ordered_k_element([6,5,4,3,2,1], 4)
print(item)

lst = [10,4,5,8,6,11,26]
el = select(lst, 0, len(lst)-1, 7)
print(el)
