# Allow up to 3 attempts
# if the user types yes, print "Glad we are on the same page"
# Otherwise, print "3 Strikes, You are Out!"

count = 0

while count < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page")
        break
    count += 1
else:
    print("3 Strikes, You are Out!")