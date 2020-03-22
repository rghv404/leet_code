'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

'''

# the most optimal soltuion is to reduce the sarch space taking advantage of asceding order of rows and col (top to bottom)
# it is not possible to do O(logmn) in thsi case cause the matrix as a series is not sorted

def searchMatrix(matrix, target):
	# start form bottom left and check the val and icnrement row, col accoridngly
	if not matrix:
		return False
	row, col = len(matrix) - 1, 0
	while col < len(matrix[0]) and row >= 0:
		if matrix[row][col] > target:
			row -= 1
		elif matrix[row][col] < target:
			col += 1
		else:
			return True
	return False

# another similar question coudl be where the matrix in as ereies is sorted
# we can again implement the above approach and solve O(n+m) time but the most optimal approach of O(logmn)
# can be acheived in this scenario as well as shown below

def searchMatrix_series(matrx: [[int]], target:int)-> bool:
	if not matrix:
		return False
	m, n = len(matrix), len(matrix[0])
	l, r = 0, m*n - 1
	# essentailly treating 
	while l <= r:
		mid = (l+r)//2
		currElem = matrix[mid//n][mid%n]
		if currElem == target:
			return True
		elif currElem > target:
			r = mid - 1
		else:
			l = mid + 1
	return False

ip = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(searchMatrix(ip, 9))