'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

    A[i] == B[j];
    The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3

Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

 

Note:

    1 <= A.length <= 500
    1 <= B.length <= 500
    1 <= A[i], B[i] <= 2000

'''
import collections
# this problem is infact a clever rendition of longest common subsequence problem which is a introductory problemn
# of dynamic programming. we'll sove it here with a couple of methods
def maxUncrossedLines(A: [int], B: [int]) -> int:
	# basically calling helper
	n, m = len(A), len(B)
	mem = [-1 for _ in range(0,n*m)]
	return helper_mem(A, B, len(A)-1, len(B)-1, mem)

def helper_recursion(A,B,n,m)->int:
		if n < 0 or m < 0:
			return 0
		if A[n] == B[m]:
			return 1 + helper(A,B,n-1,m-1)
		return max(helper(A, B, n, m-1), helper(A, B, n-1, m))

# above can be streamlined with memoization as there are many duplicatre recursion stacks
#an array of size of n*m can be used to store prev calculated comaprisons
def helper_mem(A:[int], B:[int], n:int, m:int, mem:[int]):
	if n < 0 or m < 0:
		return 0
	
	if mem[n*m] != -1: 
		return mem[n*m]

	if A[n] == B[m]:
		ans = 1 + helper_mem(A,B,n-1,m-1,mem)
	else:
		ans = max(helper_mem(A,B,n,m-1,mem), helper_mem(A,B,n-1,m,mem))
	mem[n*m] = ans
	return ans

# now we've figures out memoization we can work on bottom up approach using dynamic programming
def maxUncrossedLines_BU(A: [int], B: [int]) -> int:
	n,m = len(A), len(B)
	#instead of a 2d array we can also use a dictionary where key would be tuple i, j
	dp = collections.defaultdict(int)
	for i in range(n):
		for j in range(m):
			# if characters are equal then 1 + ans upto that string
			if A[i] == B[j]:
				dp[i, j] = dp[i-1, j-1] + 1
			else:
				dp[i, j] = max(dp[i-1, j], dp[i, j-1])
	return dp[n-1, m-1]

# the above solution takes O(n**2) time and O(n**2) space, we can reduce the space by to O(n) -- bigest list
def maxUncrossedLines_BU_ON(A: [int], B: [int]) -> int:
	n, m = len(A), len(B)
	if n < m: return maxUncrossedLines_BU_ON(B, A)
	dp = [0]*(m+1)
	for i in range(n):
		prev = 0
		for j in range(m):
			curr = dp[j+1]
			dp[j+1] = 1 + prev  if A[i]==B[j] else max(dp[j+1], dp[j])
			prev = curr
			print(dp)
	return dp[m]

A = [2,5,1,2,5]
B = [10,5,2,1,5,2]
res = maxUncrossedLines_BU_ON(A,B)
print(res)