'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
'''

# the naivee method is to basically from every index to next index see if count of zeroes and 1 are qeual and keep a count of max len

def findMaxLength_naivee(nums: [int]) -> int:
	maxLen = 0
	for i in range(len(nums)):
		zeroes, ones = 0, 0
		for j in range(i+1, len(nums)):
			if nums[j] == 0:
				zeroes += 1
			else:
				ones += 1
		if zeroes == ones:
			maxLen = max(maxLen, 2*zeroes)
	return maxLen

# the above solution works in O(n**2) time and O(1) space

# the O(N) time solution is basically keep a dictionary of counts as keys and index as values
# now the key counts is affected such that if we see 0 we decrement count and add index as value to this count
# and if we see 1 we increment the count and store the index as value. 
# When we reach the same count again that means that the current index is where the number of 1s and 0s are same
# we calcualte the length of equal number of 1s and 0s determing whether it's the global max or not

def findMaxLength(nums: [int]) -> int:
	maxLen = 0
	bucket = {0:-1}
	count = 0
	for i, val in enumerate(nums):
		if val == 0:
			count -= 1
		else:
			count += 1
		if count not in bucket:
			bucket[count] = i
		else:
			maxLen = max(maxLen, i - bucket[count])
	return maxLen


ip = [0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1]
ip = [0,1,0,1,0,0,1]
ip = [1,0]
res = findMaxLength(ip)
print(res)
