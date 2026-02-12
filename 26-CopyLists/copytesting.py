# Copying lists
# =================
# Copying lists is a common task in Python. There are several ways to do it, each with its own advantages and disadvantages. Here are some of the most common methods:
# 1. Using the `copy()` method
# The `copy()` method creates a shallow copy of the list. This means that it creates
# a new list object, but the elements in the new list are references to the same objects in the original list. If you modify an element in the new list, it will also affect the original list.
letters = ['a','b','c']
letters_copy = letters.copy()
letters_copy.append('d')
letters.pop()
print('Original list:', letters)
print('Copied list:', letters_copy)


