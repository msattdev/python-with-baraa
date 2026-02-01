# Check for missing names in a list
names = ["Alice", "Bob", "Charlie","", "David"]
for name in names:
    if name == "":
        print("BREAK BREAK BREAK! Missing name found!")
        break
    print(f"Name: {name}")
else:
    print("All names are present.")