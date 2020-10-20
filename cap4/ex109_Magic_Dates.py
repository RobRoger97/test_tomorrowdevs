from ex106_Days_in_a_Month import dayInMonth

def isMagicDate(d,m,y):
    if d*m==y%100:
        return 1
    else:
        return 0

def main():
    for year in range(1900,2000):
        for month in range(1,13):
            for day in range(1,dayInMonth(year,month)+1):
                if isMagicDate(day,month,year):
                    print("%02d/%02d/%04d is a magic date." %(day,month,year))


#Call the main function
main()