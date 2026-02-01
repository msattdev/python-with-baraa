# For loop with an else and a break
items = [1,3,5,7,9]
for item in items:
    if item % 2 == 0:
        print(item)
        break
else:
    print("All numbers are odd!") # Will only print if all numbers are odd and there is no for loop break