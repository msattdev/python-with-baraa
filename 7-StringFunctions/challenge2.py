# Clean the string
# "968-Maria, ( D@T@ Engineer );; 27y  "
# needs to be "name: maria | role: data engineer | age: 27"

messy_string = "968-Maria, ( D@T@ Engineer );; 27y  "
messy_string = messy_string.replace('968-','').replace('D@T@','Data').replace('@','a').replace(';','').replace(',','').replace(')','').replace('(','').replace('y','').strip().lower()
messy_string = f"name: {messy_string.split()[0]} | role: {' '.join(messy_string.split()[1:-1])} | age: {messy_string.split()[-1]}"
# messy_string = messy_string.replace('968-','').replace('@','a').replace(';','').replace(',','').replace(')','').replace('(','').strip().lower()
# messy_string = messy_string.replace(' ','')
print(messy_string)