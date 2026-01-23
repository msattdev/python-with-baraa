# Types 
name = 'Baraa'
print(type(name))  # str

age = 35
print(type(age))  # int
# print('Your age is: ' + age)  # This will raise an error since 'age' is an int
print('Your age is: ' + str(age))  # Correct way to concatenate int with str