# Iterator
letters = ['a', 'b', 'c']
# Using an iterator to loop through the list
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list) # ['A'], ['A', 'B'], ['A', 'B', 'C']