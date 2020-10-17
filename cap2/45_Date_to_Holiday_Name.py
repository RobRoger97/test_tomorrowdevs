#Read the day and the month from user
day = int(input("Enter the day: "))
month = input("Enter the month: ")

#If the month and day match one of the holidays listed previously then your program should display the
#holiday’s name. Otherwise your program should indicate that the entered month and
#day do not correspond to a fixed-date holiday.
if day==1 and month=="January":
    holiday = "New Year’s Day"
elif day==1 and month=="July":
    holiday = "Canada Day"
elif day==25 and month=="December":
    holiday = "Christmas Day"
else:
    holiday = ""

#Display result
if holiday == "":
    print("The entered month", month,"and day", day, "do not correspond to a fixed-date holiday.")
else:
    print(day,month,"correspond to", holiday)