'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

# naive solution is to find the first island block and then impl sort of a dfs traversal, incermeenting sum for each
# adjacent block which is either boundary or 0

class Solution:
	def __init__(self):
		self.perimeter = 0

	def islandPerimeter(self, grid: [[int]]) -> int:
		def dfs(r:int, c:int)->int:
			if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c] == 1:
				grid[r][c] = 2 # set to something else so we cycle to same cells again
				dfs(r-1,c)
				dfs(r+1,c)
				dfs(r,c-1)
				dfs(r,c+1)
			elif r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
				self.perimeter += 1

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					dfs(i, j)
					print(self.perimeter)
					return self.perimeter
		return self.perimeter

# the above approach is intuitive and apx works in O(mn) time, we stil end up revisiting the recursive stack 
# more than once for each cell even when we're setting it up as 2

# the other intuitive aproach is to basically use the fact aht we're visiting each cell left to right and top to 
# bottom, thus only hceking left and up cell shoudl suffice 

def islandPerimeter(grid: [[int]]) -> int:
	perimeter = 0
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == 1:
				perimeter += 4

				# now if the up cell is 1 then decrement result by 2 (1 for each cell)
				if r > 0 and grid[r-1][c] == 1: perimeter -= 2
				# similarly for left cell
				if c > 0 and grid[r][c-1] == 1: perimeter -= 2
	return perimeter


ip = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

ip = [[0,1,1,0],
	[1,1,1,1],
	[0,1,0,1],
	[1,0,0,1]]

ip = [[0,0,1,1]]



res = Solution().islandPerimeter(ip)

res = islandPerimeter(ip)
print(res)
		