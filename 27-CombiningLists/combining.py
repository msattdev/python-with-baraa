# Combining Lists
letters = ['a','b','c']
numbers = [1,2,3]
# Using the + operator
# combined = letters + numbers
# print(combined) # ['a', 'b', 'c', 1, 2, 3]

# Using the nested list option
combined = [letters, numbers]
print(combined) # [['a', 'b', 'c'], [1, 2, 3]]

# Using the * operator
print(letters * 2) # ['a', 'b', 'c', 'a', 'b', 'c']

# Using the extend() method
numbers.extend(letters)
print(letters) # ['a', 'b', 'c']
print(numbers) # [1, 2, 3, 'a', 'b', 'c']