# Print only the weekdays from a list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    if day in ["Saturday", "Sunday"]:
        continue
    print(day)