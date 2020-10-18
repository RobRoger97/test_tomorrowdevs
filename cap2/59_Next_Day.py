#Read a date from the user
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

# Determine if it is a leap year
if year % 400 == 0:
    isLeapYear = True  
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False
    
#Determinate the next day
if (month%2==1 and month<=7) or (month%2==0 and month>7): 
    if day==31 and month==12:
        day=1
        month=1
        year=year+1 
    elif day==31:
        day=1
        month=month+1
    else:
        day=day+1
elif (month%2==0 and month<7) or(month%2==1 and month>8) :
    if month!=2 and day==30:
        day=1
        month=month+1
    elif month==2:
        if isLeapYear and day==29:
            day=1
            month=3
        elif day==28 and isLeapYear==False:
            day=1
            month=3
    else:
        day=day+1

#Display the result
print("The day immediately after that is %d-%02d-%02d" %(year,month,day))