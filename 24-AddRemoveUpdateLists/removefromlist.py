letters = ['a', 'b', 'c', 'c', 'd', 'e']

letters.remove('c') # remove the first occurrence of 'c' from the list
print(letters)

letters.remove('c') # remove the next occurrence of 'c' from the list
print(letters)

letters.pop(1) # remove the item at index 1 (which is 'b') from the list
print(letters)

removed = letters.pop(2) # remove the item at index 2 (which is 'e') from the list and store it in a variable
print('Removed item:', removed)
print(letters)