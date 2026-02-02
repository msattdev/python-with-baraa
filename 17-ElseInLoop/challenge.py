# Check whether any filename appears more than once
files = ['data1.csv', 'data2.csv', 'data3.csv', 'data1.csv']
files_seen = []
for file in files:
    if file in files_seen:
        print(f"Duplicate file found: {file}")
        break
    files_seen.append(file)   
else:
    print("No duplicates found!")