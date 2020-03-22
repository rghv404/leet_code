def searchMatrix(matrix, target):
    if matrix:
        row,col,width=len(matrix)-1,0,len(matrix[0])
        while row>=0 and col<width:
            if matrix[row][col]==target:
                return [row, col]
            elif matrix[row][col]>target:
                row=row-1
            else:
                col=col+1
        return [-1,-1]

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 1101
print(searchMatrix(matrix, target))