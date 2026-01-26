import math
# Rounding 
# Absolute
print(abs(2 - 10))

prize = 35.54657435435
print(round(prize))
print(math.floor(prize))
print(math.ceil(prize))
print(round(prize, 2))
print(round(prize, 1))
print(math.trunc(prize))  # Removes decimal part without rounding
print(type(int(prize)))  # Converts to int, similar to trunc