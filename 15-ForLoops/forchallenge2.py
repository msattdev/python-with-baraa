# Print a left-aligned pyramid pattern using for loops
for row in range(1,7):
    for col in range(row):
        print('*', end='')
    print()
