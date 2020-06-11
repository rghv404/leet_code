'''Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000. '''

# this problem was solve in April challenge using a naivee and a dict method in both O(n**2) time and O(n) time
# here i'm trying a diff solution, I think it can work using a two pointer approach and inc/dec pointer accoridngt to the bigger count
# let's see

def findMaxLength_stupid(nums: [int]) -> int:
	o = sum([1 for num in nums if num==0])
	z = len(nums) - o
	i, j = 0, len(nums) - 1
	if o==z: return 2*o
	bigger = 0 if o > z else 1
	while i <= j or o == z:
		if nums[i] == nums[j] == bigger:
			 
			if abs(o-z) >= 2:
				i += 1
				j -= 1
				step = 2
			else:
				j -= 1
				step = 1
			if bigger == 1:
				z -= step
			else:
				o -= step
		elif nums[i] == bigger:
			i += 1
			step = 1
		elif nums[j] == bigger:
			j -=  1
			step = 1
		else: # both are minority, little tricky cause we don't want to dec minoriuty by 
		#2 but 1 cause one end of minoruty will dfnitley contribute to contig subarray
			if nums[i+1] == bigger:
				i += 1
			elif nums[j-1]==bigger:
				j -= 1
			else:
				i += 1
				j -= 1

		# fuck this got complicated too quickaly, when the fuck will I end the if else trap of my life DAMMIT


# going back to usual method of bucketing where count is dec on zero and inc on 1 and the count is the key
# such that
def findMaxLength(nums: [int]) -> int:
	bucket, count = {0:-1}, 0
	maxLen = 0
	for i, num in enumerate(nums):
		if not num:
			count -= 1
		else:
			count += 1
		if count not in bucket:
			bucket[count] = i
		else:
			maxLen = max(maxLen, i - bucket[count])
	return maxLen

arr = [0,1,]



