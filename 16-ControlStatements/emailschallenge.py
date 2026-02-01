# Filter out unsafe emails
emails = ['asa@gmail.com','bademail.virus','test@test.org','anotherbademail@.virus','goodemail@gmail.com']

for email in emails:
    if email.endswith(('.virus', '.malware')):
        print(f"Unsafe email detected for ({email}); terminating loop.")
        break
    print(f"Safe email: {email}")