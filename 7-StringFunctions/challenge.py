# Convert the messy phone number into a clean number format with only digits
messy_phone = '+49 (176) 123-4567'
# Needs to be 00491761234567
messy_phone = messy_phone.replace('+','00').replace(' ','').replace('(','').replace(')','').replace('-','')
print(messy_phone)
# 00491761234567