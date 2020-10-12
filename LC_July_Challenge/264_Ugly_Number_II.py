'''


Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.


'''

# the idea here is that each kth number can be derived from the previous one for e.g. Kth num is U
# then k+1th num will be min of (k*2,k*3,k*5). If we can maintain a list such that all numbers are sorted 
# and the first number is 1st ugly number and so on, we can continuosly use the curr ugly num to clauclate the next one

import heapq
def nthUglyNumber(n):	
	nums = [1]
	ans = 1
	for i in range(1, n+1):
		ans = heapq.heappop(nums) # this is the ith ugly number 
		heapq.heappush(nums, ans*2)
		heapq.heappush(nums, ans*3)
		heapq.heappush(nums, ans*5)
		while nums[0] <= ans: # keep popping until we get to the next ugly number so if curr ans is 2 then list in first loop will be 2,3,5 and we'll pop to get to the next ugly numnber in next loop that is 3
			heapq.heappop(nums)
		
	return ans

n = 10
res = nthUglyNumber(n)
print(res)



