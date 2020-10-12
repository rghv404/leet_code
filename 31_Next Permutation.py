'''


Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''

# we could do it naivelly to produce all perm in lexi order and then return the n+1 asked to return
# This takes O(n!) run time and O(n) space ignoring the recursive stack space


# the single pass solution si rather interseting as it generates the next perm in linear time
# the idea is that since we're generating teh next lexi perm we can repalce the first non incresing pair of elements
# from the end and for that element. Search the just larger element in the right side of the array.
# Replace the two elements and then sort teh right side of the array from i-1 to generate the just larger perm 
def nextPermutation(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(start:int, end:int):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    n = len(nums)
    i = n - 1
    while i > 0:
        if nums[i] > nums[i-1]:
            break
        i -= 1
    # in worst case i will be zero after above loop indicating the list is sorted in dec order all throughout
    # and next perm will be obtained by reversing the order
    if i==0:
        reverse(i, n-1)
        return
        
    # otherwise we find the just larger number after i-1 -- won't be the min of the right cause that could be way less than i-1 number
    justLargerNum, justLargerIdx = nums[i], i # number at i obviousl greater than i-1
    k = i+1
    while k < n:
        # keep store of the larger than i-1 number but lesser than current just larger number must replace on equal as well to handle duplicates
        if nums[k] > nums[i-1] and nums[k] <= justLargerNum:
            justLargerIdx = k
            justLargerNum = nums[k]
        k += 1

    # replace the i-1 with justLargerIdx
    nums[i-1], nums[justLargerIdx] = nums[justLargerIdx], nums[i-1]
    # print(nums)

    # now to get next lexi perm is to reverse all number post i-1 to get in order
    reverse(i, n-1)

ip = [1,5,8,4,7,6,5,3,1]
ip = [1,2,3,4]
ip = [1,4,1]
ip = [2,3,1,3,3]

nextPermutation(ip)
print(ip)


