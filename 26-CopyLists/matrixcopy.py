# Copying matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_copy = matrix.copy()
matrix.pop()
matrix[0][0] = 0
print('Original matrix:', matrix)
print('Copied matrix:', matrix_copy) # Shallow copy, changes in original matrix will affect the copied matrix