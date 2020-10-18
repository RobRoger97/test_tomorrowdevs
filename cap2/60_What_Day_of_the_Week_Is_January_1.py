import math

#Read the year from user
year = int(input("Enter an year: "))

#Compute formula
day_of_the_week = (year+math.floor((year-1)/4)-math.floor((year \
    -1)/100)+math.floor((year-1)/400))%7

#Associate the integer with the week's day
if day_of_the_week==0:
    day = "Sunday"
elif day_of_the_week==1:
    day = "Monday"
elif day_of_the_week==2:
    day = "Tuesday"
elif day_of_the_week==3:
    day = "Wednesday"
elif day_of_the_week==4:
    day = "Thursday"
elif day_of_the_week==5:
    day = "Friday"
elif day_of_the_week==6:
    day = "Saturday"

#Display the result
print("%d-01-01 is on the %d day: %s" %(year,day_of_the_week,day))