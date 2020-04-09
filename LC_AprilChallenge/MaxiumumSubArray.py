''' Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4], Output: 6 Explanation: [4,-1,2,1] has the
largest sum = 6. Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle. '''


# using kadanes algo we bascially keep two pointer a local max and a global max
# local max check whther the sum coming from previous nums is greater or not thatn the curren num
# and gloabl max keeps score of whether the local max is acutally max of all local maxes we've seen yet
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        # using Kadanes' algo
        if not nums:
        	return
        localMax = globalMax = nums[0]
        for i in range(1, len(nums)):
        	localMax = max(localMax+nums[i], nums[i]) # whether the localMax is greater than curr num, handles negative integers
        	globalMax = max(globalMax, localMax)
       	return globalMax


	# implement using divide and conquer approach

	def maxSubArray_DNC(self, nums:[int]) -> int:
		# similar to merge array
		


ip = [-1,-2,3,-1,5,-4]
ans = Solution().maxSubArray(ip)
print(ans)