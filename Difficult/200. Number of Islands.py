'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

# the idea is to do a dfs search horizontally andn vertically wheevenr a root iusland is fouind
def numIslands_dfs(grid: [[str]]) -> int:
	numIsland = 0

	def dfs(row:int, col:int):
		if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
			 return
		if grid[row][col] == 1:
			grid[row][col] = 0
			dfs(row+1, col)
			dfs(row, col+1)
			dfs(row-1, col)
			dfs(row, col-1)

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == 1:
				dfs(row, col)
				numIsland += 1
	return numIsland
# above aprroach works and is the DFS appraoch, TC: O(m*n) and space : O(m*n)

# below approach is bfs where we visit one node and if it is roor we visit it's nbegjbprs in 
# BFS manner
def numIslands_bfs(grid: [[int]]) -> int:

	numIsland = 0
	def bfs(r: int, c: int, nr: int, nc: int):
		neighbors = [(r, c)]
		while neighbors:
			row, col = neighbors.pop()
			if row - 1 > 0 and col < nc and grid[row-1][col] == 1:
				grid[row-1][col] = 0
				neighbors.append((row-1, col))
			
			if row + 1 < nr and col < nc and grid[row+1][col] == 1:
				grid[row+1][col] = 0
				neighbors.append((row+1, col))

			if row < nr and col - 1 > 0 and grid[row][col-1] == 1:
				grid[row][col-1] = 0
				neighbors.append((row, col-1))

			if row < nr and col + 1 < nc and grid[row][col+1] == 1:
				grid[row][col+1] = 0
				neighbors.append((row, col+1))


	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == 1:
				numIsland += 1
				grid[row][row] = 0
				# initiate BFS
				bfs(row, col, len(grid), len(grid[0]))
		return numIsland

grid = [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
grid = [[1,1], [0,0], [1,0]]
grid = [[1,1,1],[0,1,0],[1,1,1]]
# grid = [[1,0,1,1,0,1,1]]
# res1 = numIslands_dfs(grid)
res2 = numIslands_bfs(grid)
print(res2)