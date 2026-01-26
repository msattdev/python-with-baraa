email = "mattsattdev@gmail.com"
phone = '123-1231'
username = 'msattdev'
#Allow reg if any field is filled
print(any([email,phone,username]))

# allow reg if ALL fields are filled
print(all([email,phone,username]))