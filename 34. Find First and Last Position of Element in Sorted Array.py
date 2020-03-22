'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


'''

# it's basically a modified version of binary search as in when we find the target value we 
# do another bin search to fin the left and right bouyndary

def searchRange(nums: [int], target: int) -> [int]:
	l, r = 0, len(nums) - 1
	while l <= r:
		mid = (l + r)//2
		if nums[mid] == target:
			return [findLeft(nums, l, mid, target), findRight(nums, mid, r, target)]
		elif nums[mid] > target:
			r = mid - 1
		elif nums[mid] < target:
			l = mid + 1
	return [-1, -1]

def findLeft(arr, left, right, target):
	while left < right:
		mid = (left+right)//2
		if arr[mid] == target and arr[mid-1] < target:
			return mid
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return left

def findRight(nums, left, right, target):
	while left < right:
		mid = (left+right)//2
		if nums[mid] == target and nums[mid+1] > target:
			return mid
		elif target < nums[mid]:
			right = mid-1
		else:
			left = mid + 1
	return right


def binInsert(nums:[int], target: int):
	def getIndex(nums:[int], target: int) -> int:
		l, r = 0, len(nums) - 1
		while l<=r:
			mid = (l+r)//2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				r = mid - 1
			else:
				l = mid + 1
		return l

	index = getIndex(nums, target)
	return nums[:index] + [target] + nums[index:]

arr = [5,7,7,8,8,10]
res = searchRange(arr, 8)
print(res)

arr = []
res = binInsert(arr, 0)
print(res)
