# Continue statement
names = ["Alice", "Bob", "", "David"]
for name in names:
    if name == "":
        print("Empty value detected, skipping...")
        continue
    print(f"Name: {name}") 