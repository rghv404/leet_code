'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''

# naivee solution is to keep summing upto i digits from 1 to i using the sum 1 to n sum formular
# and as soon as sum exceeds n return that level
def arrangeCoins_loop(n: int) -> int:
	ans,i = 1, 1
	while ans < n:
		i += 1
		ans = i*(i+1)//2
	return i if ans==n else i-1

# another solution is use the mathematical folumar k(k+1) <= 2N and solve for k directly instead of
# going in loop to find appropiate k
def arrangeCoins(n: int) -> int:
	return int((2*n + 0.25)**0.5 - 0.5)

n = 5
res = arrangeCoins(n)
print(res)