# Check if a user's name is not empty and the age is greater than or equal to 18
from operator import is_


username = 'Matt'
age = 18
print(username and age >= 18)

# Check if the password is at least 8 characters long and does not contain spaces
password = 'password123'
space_count = password.count(' ')
print((len(password) >= 8) and space_count == 0)

# Check if a user's email is not empty, contains '@', and ends with '.com'
user_email = 'test@123.com'
    
print(user_email and user_email.count('@') == 1 and user_email.endswith('.com'))

# Check if a username is a string, is not None, and is longer than 5 characters
user_name = 'MattSatt'
print(isinstance(user_name, str) and user_name is not None and len(user_name) > 5)

# Check if the user is either an admin or moderator and either they're not banned or they've verified their email.
user = 'MattSatt'
is_admin = False
is_moderator = True
is_banned = False
is_email_verified = True
print((is_admin or is_moderator) and (not is_banned or is_email_verified))