'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


'''
# naiveee solution works in O(2**(m+n)) time cause at every step we have two option and 
# we make a lot of duplicate choices
def minPathSum_naiveee(grid: [[int]]) -> int:

    def helper(r:int,c:int,currSum:int)->int:
        if r == n-1 and c == m-1:
            # we're at bottom right
            return currSum
        elif r == n-1:
            return helper(r,c+1,currSum+grid[r][c+1])
        elif c == m-1:
            return helper(r+1,c,currSum+grid[r+1][c])
        return min(helper(r,c+1,currSum+grid[r][c+1]), helper(r+1,c,currSum+grid[r+1][c]))
    res = grid[0][0]
    n,m = len(grid), len(grid[0])
    res = helper(0,0,res)
    return res

# the dp approach is something I almost figured out just got cnfused at breaking down the cell level value
# anyway we do a bottom up approach and then add the min of next cell traversal option
# this become down cell and right cell for bootm row adn last column. We are sure to reach the min sum with this approach
def minPathSum(grid: [[int]]) -> int:
    r, c = len(grid), len(grid[0])
    for i in range(r-1, -1, -1):
        for j in range(c-1,-1,-1):
            if i == r - 1 and j != c-1: #last row but excluding bottomright
                grid[i][j] += grid[i][j+1]
            elif i != r - 1 and j == c-1: #last column but excluding bottomright
                grid[i][j] += grid[i+1][j]
            elif i != r - 1 and j != c-1: #not last row or col or bottomright
                grid[i][j] += min(grid[i][j+1], grid[i+1][j])
    return grid[0][0]


ip = [[1,3,1],[1,5,1],[4,2,1]]
res = minPathSum(ip)
print(res)