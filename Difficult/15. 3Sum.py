'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import collections
class Solution:
        
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 2:
#             return []
#         countBucket = collections.Counter(nums)
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 num1, num2, target = nums[i], nums[j], - nums[i] - nums[j]
#                 triplet = [num1, num2, target]
#                 triplet.sort()
#                 if tuple(triplet) not in self.res:
#                     if target == num1 and target == num2 and countBucket[target] > 2:
#                         self.res.add(tuple(triplet))
                        
#                     elif ((target == num1 and target != num2) or (target == num2 and target != num1)) and countBucket[target] > 1:
#                         self.res.add(tuple(triplet))

#                     elif target in nums and target not in (num1, num2) and countBucket[target] > 0:
#                         self.res.add(tuple(triplet))

#         return list(self.res)
    def valid(self, tup: [int, int, int], bucket:{int}) -> bool:
        a, b, t = tup
        if t == a and t != b and bucket[t] > 1:
            return True
        elif t == b and t != a and bucket[t] > 1:
            return True
        elif t != a and t != b:
            return True
        return False

    def threeSum(self, nums: [int]) -> [[int]]:
        # above was more of a generic solution to fidn specific target and not just 0
        # for 0 we can separate the array in positive and negative, zip both and look for target in bucket
        if len(nums) < 2:
            return []
        positiveLst = [num for num in nums if num>0]
        negativeLst = [num for num in nums if num<0]
        res = set()
        count_bucket = collections.Counter(nums)
        if count_bucket[0] > 2:
            res.add((0,0,0))

        for num1 in positiveLst:
            for num2 in negativeLst:
                target = -num1 - num2
                triplet = [target, num2, num1] if target < num2 else [num2, target, num1] if target < num1 else [num2, num1, target]
                if target in count_bucket and self.valid((num1, num2, target), count_bucket):
                    if tuple(triplet) not in res:
                        print(triplet, num1, num2, target)
                        res.add(tuple(triplet)) 
        return list(res)


ip = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
res = Solution().threeSum(ip)
print(res)