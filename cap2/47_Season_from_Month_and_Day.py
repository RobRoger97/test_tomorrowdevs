# Read the date from the user
m = input("Enter the name of the month: ")
d = int(input("Enter the day number: "))

# Determine the season
if m == "January" or m == "February":
    season = "Winter"
elif m == "March":
    if d < 20:
        season = "Winter"
    else:
        season = "Spring"
elif m == "April" or m == "May":
    season = "Spring"
elif m == "June":
    if d < 21:
        season = "Spring"
    else:
        season = "Summer"
elif m == "July" or m == "August":
    season = "Summer"
elif m == "September":
    if d < 22:
        season = "Summer"
    else:
        season = "Fall"
elif m == "October" or m == "November":
    season = "Fall"
elif m == "December":
    if d < 21:
        season = "Fall"
    else:
        season = "Winter"

# Display the result
print(d, m, "is in", season)