# Read the birth date from the user
m = input("Enter the name of the birth month: ")
d = int(input("Enter the birth day number: "))

# Determine the Zodiac Sign
if (m == "December" and d>=22) or \
    (m == "January" and d<=19):
    sign = "Capricorn"
elif (m == "January" and d>=20) or \
    (m == "February" and d<=18):
    sign = "Acquarius"
elif (m == "February" and d>=19) or \
    (m == "March" and d<=20):
    sign = "Pisces"
elif (m == "March" and d>=21) or \
    (m == "April" and d<=19):
    sign = "Aries"
elif (m == "April" and d>=20) or \
    (m == "May" and d<=20):
    sign = "Taurus"
elif (m == "May" and d>=21) or \
    (m == "June" and d<=20):
    sign = "Gemini"
elif (m == "June" and d>=21) or \
    (m == "July" and d<=22):
    sign = "Cancer"
elif (m == "July" and d>=23) or \
    (m == "August" and d<=22):
    sign = "Leo"
elif (m == "August" and d>=23) or \
    (m == "September" and d<=22):
    sign = "Virgo"
elif (m == "September" and d>=23) or \
    (m == "October" and d<=21):
    sign = "Libra"
elif (m == "October" and d>=23) or \
    (m == "November" and d<=21):
    sign = "Scorpio"
elif (m == "November" and d>=22) or \
    (m == "December" and d<=21):
    sign = "Sagittarius"

#Display result
print("Your sign is:",sign)
