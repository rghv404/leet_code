'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

'''

# my naivee solution si what my feeble and distracted mind is fixated on, traversing each possible route from every cell
# in a top down fashion incremneting possile path when reaching the botton right


def uniquePaths_naivee(m: int, n: int) -> int:
    res = 0
    def helper(r:int, c:int):
        nonlocal res
        if r == m and c == n:
            res += 1
            return
        elif r == m:
            helper(r, c+1)
        elif c == n:
            helper(r+1, c)
        else:
            helper(r, c+1)
            helper(r+1, c)
    helper(1, 1)
    return res

# above solution is crippled on a grid with 23 cols and 12 rows cause of the sheer number of traversals

# the dynamic solution tha I came up with after 40 min sof finding the goddamn pattern

def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for i in range(m)] for i in range(n)] # m is cols n is rows
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[-1][-1]

op = uniquePaths(23, 12)
# op = uniquePaths(7,3)
print(op)