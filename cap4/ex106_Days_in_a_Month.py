def dayInMonth(y,m):
# Determine if it is a leap year
#Any year that is divisible by 400 is a leap year.
    if y % 400 == 0:
        a = 1
#Of the remaining years, any year that is divisible by 100 is not a leap year.  
    elif y % 100 == 0:
        a = 0
#Of the remaining years, any year that is divisible by 4 is a leap year.
    elif y % 4 == 0:
        a = 1
#All other years are not leap years.
    else:
        a = 0

    d = 0
    if m == 1 or m==3 or m==5 or\
       m==7 or m==8 or m==10 or m==12:
        d = 31
    elif m == 2:
        if a == 1:
            d = 29
        else:
            d = 28
    elif m == 4 or m==6 or m==9 or m==11:
        d = 30
    return d

def main():
    a = int(input('Insert an year:'))
    b = int(input('Insert an month:'))
    print(dayInMonth(a, b))

if __name__ == "__main__":
        main()