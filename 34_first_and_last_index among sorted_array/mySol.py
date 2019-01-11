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
            if nums[m] == target:
                try:
                    k, j = m, m
                    while k <= r and nums[k] == target:
                        k += 1
                    while j >= l and nums[j] == target:
                        j -= 1
                    return [j+1,k-1]
                except:
                    break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [-1, -1]