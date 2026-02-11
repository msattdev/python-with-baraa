# Adding items to lists

matrix = [
    ['a', 'b', 'c'], # row 0
    ['d', 'e', 'f'], # row 1
    ['g', 'h', 'i']  # row 2
]

# matrix.append(['x', 'y', 'z']) # add a new row to the end of the matrix
# matrix.insert(1, ['a','a','a']) # add a new row at index 1
# matrix[0].append('d') # add a new item to the end of row 0
# matrix[2].insert(1, 'x') # add a new item at index 1 of row 2

# matrix[1].remove('e') # remove the first occurrence of 'e' from row 1
# matrix[-1].pop(0) # remove the item at index 0 of the last row (which is 'g')

matrix[-1] = ['x', 'y', 'z'] # replace the last row with a new row
matrix[0][0] = 'x' # replace the item at index 0 of row 0 with 'x'
matrix[1][1] = 'y' # replace the item at index 1 of row 1 with 'y'
print(matrix)