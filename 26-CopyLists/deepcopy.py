# Deep copy
import copy
matrix = [
    ['a','b'],
    ['c','d']
]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('Original matrix:', matrix)
print('Copied matrix:', matrix_copy)

# copy.copy is the same as a shallow copy, while copy.deepcopy creates a deep copy of the object. In a deep copy, all nested objects are also copied, so changes to the original object will not affect the copied object.