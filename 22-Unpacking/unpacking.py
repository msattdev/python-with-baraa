# Asterisk operator
person = ['Maria',29,'Data Engineer','Spain']
# name, *details, country = person
# print(name)
# print(details)
# print(country)

# *details, country = person
# print(details)
# print(country)

name, *details = person
print(name)
print(details)