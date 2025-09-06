"""
Matrix Rotate
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given [[1, 2], [3, 4]], which looks like this:

1	2
3	4
You should return [[3, 1], [4, 2]], which looks like this:

3	1
4	2

"""

def rotate_builtin(matrix):

    transposed = list(zip(*matrix))

    rotated = [list(row[::-1]) for row in transposed]

    return rotated

def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rotated = [[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):

            rotated[j][rows-1-i] = matrix[i][j]

    return rotated



if __name__ == "__main__":
    print(rotate([[1,2],[3,4]]))

    print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    print(rotate_builtin([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    

