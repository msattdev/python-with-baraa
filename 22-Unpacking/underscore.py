# Use underscore to ignore certain values during unpacking
person = ['Maria',29,'Data Engineer','Spain']

# name, _, role, _ = person

# print(name)
# # print(age)
# print(role)
# # print(country)

name, *_, country = person
print(name)
print(country)