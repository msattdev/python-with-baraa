# Count with lists
my_list = ['a','b','b','c','c','c','c','d','e','f']

# Count occurrences of 'a'
count_a = my_list.count('a')
print(f"The letter 'a' appears {count_a} times in the list.")

# Count occurrences of 'c' using a loop
count = 0
for x in my_list:
    if x == 'c':
        count += 1
print(f"The letter 'c' appears {count} times in the list.")

# Count occurrences of 'c'
count_c = my_list.count('c')
print(f"The letter 'c' appears {count_c} times in the list.")

# Count occurrences of 'b'
count_b = my_list.count('b')
print(f"The letter 'b' appears {count_b} times in the list.")

# Count occurrences of 'c'  
count_c = my_list.count('c')
print(f"The letter 'c' appears {count_c} times in the list.")

# Count occurrences of 'x' (not in the list)
count_x = my_list.count('x')
print(f"The letter 'x' appears {count_x} times in the list.")