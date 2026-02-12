import copy

original =  [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
]

# Assignment
copy1 = original
print("Same Object?", original is copy1, "\n") # True, both variables point to the same object in memory

# Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2) # False, copy2 is a new object
print("Shared Lists?", original[0] is copy2[0], "\n") # True, the inner lists are shared between original and copy2

# Deep Copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3) # False, copy3 is a new object
print("Shared Lists?", original[0] is copy3[0], "\n") # False, the inner lists are also copied, so they are not shared between original and copy3