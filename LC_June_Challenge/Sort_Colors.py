'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?

'''
import collections
# the obvious way is to do in nlogn time using in place pythonic sorting technique
def sortColors(nums: [int]) -> None:
	nums.sort()


#the other way is to use count sort because we know the range of numbers i.e. 0 to 2 in a two pass fashion
def sortColors_two(nums: [int]) -> None:
	bucket = collections.Counter(nums)
	i, key = 0, 0
	while i < len(nums):
		if bucket[key] == 0:
			key += 1
			continue
		nums[i] = key
		i += 1
		bucket[key] -= 1

#one pass solution
def sortColors_three(nums: [int]) -> None:
	l, r = 0 , len(nums) - 1
	curr = 0
	while curr<=r:
		if nums[curr] == 0:
			nums[curr], nums[l] = nums[l], nums[curr]
			l += 1
			curr += 1
		elif nums[curr] == 2:
			nums[curr], nums[r] = nums[r], nums[curr]
			r -= 1
		else:
			curr += 1
		print(nums) 


arr = [0,2,1,0,0,1,2,1,1,2]
# sortColors_two(arr)
sortColors_three(arr)
setInts = {1,2,3,4}
print(setInts.get(3))
print(arr)