from itertools import permutations
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        next_perm = False
        for i in range(1, n):
            a, b = nums[-i], nums[-i-1]
            if b < a:
                next_perm = True
                j = get_just_greater(nums[-i:], b)
                nums[-i-1], nums[-i+j] = nums[-i+j], nums[-i-1]
                # reversing all elements post -i
                # best inplace reversal i could come up with
                nums[-i:] = nums[-i:][::-1] 
                break
                
        if not next_perm:
            nums.reverse()

def get_just_greater(arr, target):
    curr_res = float('infinity')
    res = float('infinity')
    for i in range(len(arr)):
        if arr[i] > target and arr[i] <= curr_res:
            curr_res = arr[i]
            res = i
    return res