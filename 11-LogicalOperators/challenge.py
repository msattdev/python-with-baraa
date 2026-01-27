# Check if a user's name is not empty and the age is greater than or equal to 18
username = 'Matt'
age = 18
print(username and age >= 18)

# Check if the password is at least 8 characters long and does not contain spaces
password = 'password123'
space_count = password.count(' ')
print((len(password) >= 8) and space_count == 0)

# Check if a user's email is not empty, contains '@', and ends with '.com'
user_email = ''

print(not user_email and user_email.count('@') == 1 and user_email.endswith('.com'))

# Check if a username is a string, is not None, andis longer than 5 charatcers


# Check if the user is either an admin or moderator and either they're not banned or they've verified their email.