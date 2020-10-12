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
# the idea is basically to keep each number in a dictionary with the index as key and then iterate over the list
# chekcing in dict whether the arget is present or not
import collections
def threeSum(nums: [int]) -> [[int]]:
	bucket = collections.defaultdict(set)
	for i, num in enumerate(nums):
		bucket[num].add(i)
	print(bucket)
	res = set()

	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			target = -(nums[i]+nums[j])
			if target in bucket and bucket[target] and not set([i, j]) == bucket[target]:
				potentialSet = [nums[i], nums[j], target]
				potentialSet.sort()
				print(potentialSet)
				if tuple(potentialSet) not in res:
					res.add(tuple(potentialSet))
				bucket[target].pop() # delte target's one element because we don't want to reuse that index again
	return res

# the other solution is much more interesting as we employ a 

nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0]
res = threeSum(nums)
print(res)
