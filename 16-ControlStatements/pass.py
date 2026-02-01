# pass statement
names = ["Alice", "Bob", "", "David"]
for name in names:
    if name == "":
        # print("Empty value detected, skipping...")
        pass # Todo: handle empty names properly later
    print(f"Name: {name}") 