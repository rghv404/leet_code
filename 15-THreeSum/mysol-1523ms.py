class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = set()
        # handling all the special cases
        if n == 0:
            return []
        # if all zeroes then return [0,0,0]
        elif all(l==0 for l in nums) and n >= 3:
            return [[0,0,0]]
        # if all positive then return []
        elif all(l > 0 for l in nums):
            return []
        # all in nums till second last element
        for i in range(n-1):
            # set for the 
            s_ = set()
            for j in range(i+1,n):
                if -(nums[i] + nums[j]) in s_:
                    x = sorted([nums[i],nums[j],-(nums[i]+nums[j])])
                    x = tuple(x)
                    if x not in res:
                        res.add(x)
                else:
                    s_.add(nums[j])
        return [list(l) for l in res]
                    
                            