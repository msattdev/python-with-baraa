# Control statements in Python
names = ['john','maria','', 'kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        break
    print(f"Name = {name}")