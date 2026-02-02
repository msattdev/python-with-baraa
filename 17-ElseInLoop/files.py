# check if all files are CSV files
files = ['data1.csv', 'data2.csv', 'data3.pdf', 'data4.csv']
for file in files:
    if not file.endswith('.csv'):
        print(f"\"{file}\" IS NOT A CSV!")
        break
    print(f"Filename: {file}")
else:
    print("All files are CSVs!")