'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
import collections
class Solution:

    def singleNumber(self, nums: [int]) -> int:
   		bucket = collections.Counter(nums)
   		return [num for num, val in bucket.items() if val == 1][0]


#there's another amazing method to solve this to XOR the numbers. It's incredible that 

ip = [1,1,2]
res = Solution().singleNumber(ip)
print(res)