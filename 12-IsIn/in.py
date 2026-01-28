print('a' in 'Data')  # True

group = ['Max', 'Anna', 'Matt']
print('Matt' in group)  # True
print('John' in group)  # False

print("o" not in "python")  # True
print(3 not in [1,2,3,4,5])  # False

# Security check: ensure the domain is not banned
domain = "gmail.com"
domain2 = "spam.com"
banned_domains = ["spam.com","fake.org","bot.net"]
print(domain not in banned_domains) # True
print(domain2 not in banned_domains) # False