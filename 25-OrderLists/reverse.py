# Reversing a list
letters = ['c','a','b']
# letters.reverse() # Reverse the list in place
new_list = reversed(letters) # Create a new reversed list without modifying the original
print('Original List:', letters)
print('Reversed List:', list(new_list))
print('Original List after reversed():',letters)