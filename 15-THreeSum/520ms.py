from collections import defaultdict

class Solution:
    def threeSumm_original_sol(self, nums):
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
                    
    def threeSum(self, nums):
        # dictionary of nums and their respective frequencies
        if nums is None:
            return []
        f_dict = defaultdict(int)
        for n in nums:
            f_dict[n] += 1
        positives = [p for p in f_dict if p > 0]
        negatives = [p for p in f_dict if p < 0]
        res_ = set()
        # case where we have more than two zeroes
        if 0 in f_dict and f_dict[0] > 2:
            res_.add((0,0,0))
        for a in positives:
            for b in negatives:
                req_num = -(a+b)
                if req_num in f_dict:
                    if req_num == a and f_dict[req_num] > 1:
                        res_.add((b, a, a))
                    if req_num == b and f_dict[req_num] > 1:
                        res_.add((b, b, a))
                    if b < req_num < a:
                        res_.add((b, req_num, a))
        return list(res_)
                