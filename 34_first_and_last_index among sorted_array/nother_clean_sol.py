class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # first thought process is to search in binary manner and 
        # if foudn check within l and r for the start and end index
        # the complexity remains log(n)
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            
            if nums[l] == nums[r] == target:
                return [l, r]
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[l] < target:
                l += 1
            elif nums[r] > target:
                r -= 1
        return [-1, -1]