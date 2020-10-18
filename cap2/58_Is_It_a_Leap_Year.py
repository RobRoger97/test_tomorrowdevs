# Read the year from the user
year = int(input("Enter a year: "))

# Determine if it is a leap year
#Any year that is divisible by 400 is a leap year.
if year % 400 == 0:
    isLeapYear = True
#Of the remaining years, any year that is divisible by 100 is not a leap year.    
elif year % 100 == 0:
    isLeapYear = False
#Of the remaining years, any year that is divisible by 4 is a leap year.
elif year % 4 == 0:
    isLeapYear = True
#All other years are not leap years.
else:
    isLeapYear = False
    
# Display the result
if isLeapYear:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")