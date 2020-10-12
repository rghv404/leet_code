'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.


'''
# Since the duplicate number can be more than twice we can't find it using the sum method

# the method is find the diff b/w max num currently in teh list and what shoudl ideally be max
# sunbtract both, if'll atleast be one more than current max cause 1 dupliate is guranteed
# if it's more than 1 then we are guraanteed to have one duplicate number that many times more
# for e.g. 1,2,2,2,2,3,4, crrMx = 4, idealMx = len(bums) = 7 
# 7 - 4 = 3 which indicates atleast one number is 3 times more than it should be 
# solve it for 3x + n(n+1)//2 = sum(nums)
def findDuplicate(nums: [int]) -> int:
	idealMax = len(nums)
	currMax = max(nums) # in O(n) time
	times = idealMax - currMax
	#solve equation
	sumWithcurrMax = (currMax*(currMax+1))//2 # using 1..n sum formula
	duplicateNumber = (sum(nums)-sumWithcurrMax)//times
	return duplicateNumber


ip = [1,2,2,2,2,3,4]
ip = [1,2,3,4,4]
res = findDuplicate(ip)
print(res)