# Types 
name = 'Baraa'
print(type(name))  # str

age = 35
print(type(age))  # int
# print('Your age is: ' + age)  # This will raise an error since 'age' is an int
print('Your age is: ' + str(age))  # Correct way to concatenate int with str

age = age + 5
print(age)
age = str(age)  # Converting int to str
print(type(age))  # str
# age = age + 5  # This will now concatenate since 'age' is a str
print(age)

# Math 
password = '12wrwrwrwrw3a'
print(len(password))


if len(password) < 8:
    print('Your password is too short!')
else:
    print('Your password is long enough!')