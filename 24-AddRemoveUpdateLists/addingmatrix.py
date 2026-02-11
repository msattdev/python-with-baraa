# Adding items to lists

matrix = [
    ['a', 'b', 'c'], # row 0
    ['d', 'e', 'f'], # row 1
    ['g', 'h', 'i']  # row 2
]

matrix.append(['x', 'y', 'z']) # add a new row to the end of the matrix
matrix.insert(1, ['a','a','a']) # add a new row at index 1
matrix[0].append('d') # add a new item to the end of row 0
matrix[2].insert(1, 'x') # add a new item at index 1 of row 2
print(matrix)