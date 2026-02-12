# Sort lists
letters = ['d', 'b', 'a', 'e', 'c']
letters.sort() # Sort the list in ascending order
print(letters)
letters.sort(reverse=True) # Sort the list in descending order
print(letters)

matrix = [
    [3, 1, 2],
    [6, 4, 5],
    [9, 7, 8]
]
matrix.sort() # Sort the matrix based on the first element of each row
print(matrix)
matrix[1].sort() # Sort the second row of the matrix
print(matrix)