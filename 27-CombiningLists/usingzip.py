# Using zip
letters = ['a','b','c']
numbers = [1,2,3]
# Using zip to combine lists into a list of tuples
comb = list(zip(letters, numbers))
print(comb) # [('a', 1), ('b', 2), ('c', 3)]