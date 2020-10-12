'''


Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]


'''

def largestDivisibleSubset(nums):
	res = []
	nums.sort()
	for i, num in enumerate(nums):
		op = [num]
		for j in range(i+1, len(nums)):
			prevNum = op[-1]
			if nums[j] % prevNum == 0:
				op.append(nums[j])
		res = max(res, op, key=len)
	return res

# below DP solution solves it in O(n**2) time and O(n) space
# the jist is that at each index we should store the length of max subset from the prev divisible lasrgest number
# so dp[i] essentia;;y becomes dp[j] + 1 where dp[j] is divisible by dp[i] 
# and this value shoudl be max of all dp[j] diviisble by dp[i] for j < i
# In above partial solution we were only considering j = i-1
from operator import itemgetter
def largestDivisibleSubset_dp(nums):
	n = len(nums)
	if n<=1:
		return nums
	nums.sort()
	dp = [(0,0) for _ in range(n)]
	dp[0] = (0,1) # 1st value will be it's own subset for sure
	maxInd, maxVal = 0, 1
	for i in range(1, n):
		dp[i] = max(((j, dp[j][1]+1) for j in range(i+1) if nums[i]%nums[j]==0), key=itemgetter(1))
		if dp[i][1] > maxVal:
			maxInd, maxVal = i, dp[i][1]
		print(dp[i])

	# after the loop is over we go to dp having max val and use it's stored index (j) to build the result set
	i = maxInd
	res = [nums[i]]
	while i != dp[i][0]: # goes back to the value which holds it's own index mostly the first value's index
		i = dp[i][0]
		res.append(nums[i])
	return res



ip = [4,6,9,3,1]
# ip =[1,2,3]
# ip = [1,2,4,8]
ip = [3,1,6,9,27]
res = largestDivisibleSubset_dp(ip)
print(res)