# Logical Operators in Python
print(3 > 1 and 5 < 1)  # Logical AND: True if both conditions are true
print(3 > 1 or 5 < 1)   # Logical OR: True if at least one condition is true
print(not(3 > 1))       # Logical NOT: Inverts the boolean value

# checks if the system is under pressure
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90) # True if either CPU or memory usage is above 90%

# checking user credentials before login
email = True
password = False
print(email and password) # True if both email and password are correct