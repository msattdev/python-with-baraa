# If Else on one line
score = 50
if score >= 90:
    print("A")
else:
    print("F")

# Using ternary operator for if-else
result = "A" if score >= 90 else "F"
print(result)

# Multiple conditions in one line using nested ternary operators
# Ternary doesn't make sense for complex logic, but for demonstration:
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(grade)