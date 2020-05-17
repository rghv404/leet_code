'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

 

Note: Your solution should run in O(log n) time and O(1) space.

'''
# use binary search to divide such that when mid elemnt is odd and next elemt is same as mid then single element lies left side else right
# and vioce versa when mid is even
def singleNonDuplicate(nums: [int]) -> int:
	l,r = 0, len(nums)-1
	while l<=r:
		mid = (l+r)//2
		if mid % 2: # if odd
			if mid + 1 <  len(nums) and nums[mid] == nums[mid + 1]:
				# element lies to the left
				r = mid - 1
			elif mid - 1 > -1 and nums[mid] == nums[mid - 1]:
				l = mid + 1
			else:
				return nums[mid]
		else:
			if mid + 1 <  len(nums) and nums[mid] == nums[mid + 1]:
				# element lies to the right
				l = mid + 1
			elif mid - 1 > -1 and nums[mid] == nums[mid - 1]:
				r = mid - 1
			else:
				return nums[mid]

arr = [0,0,1,1,2]
res = singleNonDuplicate(arr)
print(res)