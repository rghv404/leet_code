def rotate_mySol(matrix):
    i = 0
    for row in zip(*matrix):
        matrix[i] = list(row[::-1])
        i += 1
    return matrix


def rotate():
    for i in range(len(matrix)):
        for j in range(i):


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
