'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            left, right = 0, 1
            while right < n:
                # case 1
                if nums[left] == 0 and nums[right] == 0:
                    right += 1
                # case 2 , the second part is only for cases where array is [1,0]
                elif (nums[left] != 0 and nums[right] != 0 ) or (nums[left] != 0 and nums[right] == 0):
                    left += 1
                    right += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
        print(nums)

ip = [0,0,0,0,5,1,4,0,6,0,7,0,8,0]

ip = [0,5,0,0,1,6]
ip = [1,0]
Solution().moveZeroes(ip)