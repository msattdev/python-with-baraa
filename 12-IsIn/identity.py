a = [1,2,3]
print(a)
b = [1,2,3]
print(b)
print(a is b)  # False, because a and b reference different objects in memory
print(a == b)  # True, because a and b have the same content


x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)  # True, because x and y have the same content
print(x is y)  # False, because x and y reference different objects in memory

email = None
print(email is not None and email != "") # True if email is not None and not an empty string