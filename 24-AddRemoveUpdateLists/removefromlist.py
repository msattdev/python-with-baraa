letters = ['a', 'b', 'c', 'c', 'd', 'e']

letters.remove('c') # remove the first occurrence of 'c' from the list
print(letters)

letters.remove('c') # remove the next occurrence of 'c' from the list
print(letters)

letters.pop(1) # remove the item at index 1 (which is 'b') from the list
print(letters)