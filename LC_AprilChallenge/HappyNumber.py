'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1**2 + 9**2 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

# looks straigh forward to me keep squaring the digit unless we get 1

# actually a number is not happy if we find a cycle in it's process of indentification
# for e.g. 4 which is not ahappy will lead to a 4
class Solution:
    def isHappy(self, n: int) -> bool:
    	numSet = set()
    	squaredNum = n
    	while squaredNum != 1:
    		print(squaredNum)
    		squaredNum = self.get_sqaures_num(squaredNum)
    		if squaredNum in numSet:
    			return False
    		numSet.add(squaredNum)
    	return True



    def get_sqaures_num(self, num:int)->int:
    	sq = 0
    	while num > 0:
    		digit = num % 10
    		sq += digit ** 2
    		num = int(num/10)
    	return sq


ip = 23
res = Solution().isHappy(ip)
print(res)
