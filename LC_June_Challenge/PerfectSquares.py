'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

import math
def numSquares_rec(n: int) -> int:

	def helper(nums:[int], start:int, currSum:int, lsts:[int]):
		# nonlocal minLength

		# if currSum == 0: # or we can also check if the currSum is already there in the sqaure list to prevent extra call
		# 	# print('good: ', lsts)
		# 	minLength = min(minLength, len(lsts))
		# 	return
		if currSum in nums:
			return 1

		minLength = float('inf')

		for i in range(start, len(nums)):
			if currSum < nums[i]:
				break
			# lsts.append(nums[i]) # not required to append to any list cause we are simply need to the min number
			# print(lsts, currSum+nums[i])
			newMin = 1 + helper(nums, i, currSum-nums[i], lsts)
			# lsts.pop() # since no list required thus no popping
			# print(minLength, newMin, currSum-nums[i], i)
			minLength = min(minLength, newMin)
			# print('popped:', lsts, currSum)
		return minLength

	lst = [i**2 for i in range(1, int(math.sqrt(n))+1)]
	print('startng with: ', lst)
	return helper(lst, 0, n, [])
	# return minLength

# the dynamic programming approach is basically the above approach with previous min number of Squares saved to 
# be reused later

def numSquares(n: int) -> int:
	# each cell will hold the min number of prefect squares to obtain that number
	dp = [float('inf') for _ in range(n+1)]
	dp[0] = 0 # base case is 0 
	
	for i in range(1, len(dp)):
		# j will be the actual square numbers we'll be using to make ith num
		j = 1
		while j*j <= i:
			dp[i] = min(dp[i], dp[i-j*j]+1) # either already minimum or obtained by adding one more to the min of a prev sqaure
			j += 1
	return dp[n]


ip = 13089
res = numSquares(ip)
print(res)
