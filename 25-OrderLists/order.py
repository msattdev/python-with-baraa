# Sort lists
letters = ['d', 'b', 'a', 'e', 'c']
# letters.sort() # Sort the list in ascending order
# print(letters)
# letters.sort(reverse=True) # Sort the list in descending order
# print(letters)
new_list = sorted(letters) # Create a new sorted list without modifying the original
reverse_list = sorted(letters, reverse=True) # Create a new sorted list in descending order
print('Original List:', letters)
print('Reversed List:',reverse_list)
print('Sorted List:',new_list)

matrix = [
    [3, 1, 2],
    [6, 4, 5],
    [9, 7, 8]
]
matrix.sort() # Sort the matrix based on the first element of each row
print(matrix)
matrix[1].sort() # Sort the second row of the matrix
print(matrix)