'''Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)'''

# the solution uisng O(N) extra space stores product of numbers in origianl array upto i from start
# and then uses the temp product array to update from the end using a temp variabl;e which stores product uptoi from end
# for e.g. --> 1,2,3,4 --> prod = 1,1,2,6 -- this prod array rep at each index prod upto i from left
# then in another iteration we can use the prod and orig arr from the end to insert prod from right store in temp var and this tem muiltiplied with what;'s in prod array
# 

def productExceptSelf_ON(nums: [int]) -> [int]:
	# init prod array
	prod = [0] * len(nums)
	
	# iterate the orig array and update prod with product upto i from left
	temp = 1
	for i in range(len(nums)):
		prod[i] = temp # assign temp to prod
		temp *= nums[i] # store prod upto i in temp

	temp = 1
	for i in range(len(nums) - 1, -1, -1): # iterate from the end
		prod[i] *= temp # mulitply what's in prod at i (i.e  prod upto i form left) with temp (prod upto i from right)
		temp *= nums[i] # stores prod upto i from right

	return prod


'''
Another solution to solve it in O(1) space is along the though that log(1*2*3*4) --> log(1) + log(2) + log(3) + log(4)
so at i we can populate with antilog( log(prod) - log(i))
'''
import math
from functools import reduce
def productExceptSelf(nums: [int]) -> [int]:
	eps = 1e-9
	prodVal = 0
	for num in nums:
		prodVal += math.log10(num) if num != 0 else 0
	for i in range(len(nums)):
		nums[i] = int(eps + pow(10, (prodVal - math.log10(nums[i])))) if num != 0 else 0
	return nums

arr = [1,2,3,4]
arr = [0,0]
res = productExceptSelf(arr)
print(res)
