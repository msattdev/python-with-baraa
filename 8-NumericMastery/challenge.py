import random
# Generate a random number between 1 and 100
# And then check if that number is even

x = random.randint(1,100)
if x % 2 == 0:
    print(f'{x} is an even number!')
else:
    print(f'{x} is an odd number!')