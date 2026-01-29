# Baraa Challenge
# Must not be empty
# Must contain '.' and '@'
# Must contain exactly one '@' symbol
# Must end with '.com', '.org', or '.net'
# Must not be longer than 254 characters

user_email = 'hacktest@test.com'
user_email = user_email.strip()

if user_email != '':
    if '@' in user_email and '.' in user_email:
        if user_email.count('@') == 1:
            if user_email.endswith(('.com','.org','net')):
                if len(user_email) <= 254:
                    print("Your email address is valid!")
                else:
                    print("Email must not be longer than 254 characters")
            else:
                print("Email must end with .com, .org, or .net")
        else:
            print("Email must only contain 1 '@' symbol")
    else:
        print("Email must contain an '@' and a '.'")
else:
    print("Email must not be empty")