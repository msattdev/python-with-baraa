# Real world use case for using zip
from os import name


names = ['Alice','Bob','Charlie']
ids = [101, 102, 103]
# Using zip to create a dictionary of names and ids
name_id_list = list(zip(names, ids))
name_id_dict = dict(zip(names, ids))
print(name_id_list) # [('Alice', 101), ('Bob', 102), ('Charlie', 103)]
print(name_id_dict) # {'Alice': 101, 'Bob': 102, 'Charlie': 103}