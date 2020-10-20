#Define ordinalDate Function
def ordinalDate(d,m,y):
#Leap year
    if y % 400 == 0:
        bis = 1
    elif y % 100 == 0:
        bis = 0
    elif y % 4 == 0:
        bis = 1
    else:
        bis = 0


    if bis == 1:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
    x = 1
    days = 0
    days_before=0
    if 2 <= m <= 12 and d<=months[m-1]:
        while x < m:
            days_before= months[m-2] + days_before
            m = m-1
        days = days_before+d
    elif m==1 and d<=31:
        days=d
    else:
        print('The date you entered is incorrect')

    return days

#Define main function
def main():
#Read year,month anc day from the user
    datey = int(input('Enter a year:'))
    datem = int(input('Enter a month:'))
    dated = int(input('Enter a day:'))

#Display the result
    print(datey,ordinalDate(dated, datem, datey))

if __name__ == "__main__":
        main()