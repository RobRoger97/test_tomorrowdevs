#Check days in month depending on the type og year
def bis(y): 
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

    return months, bis

def greg_date(y,d, r=0):
    bises = bis(y)
    bi = bises[1] #check if year is bis

    d = d + r
    if d >365 and bi==0:
        x = d//365
        y = y+x
        d = d%365
    elif d > 366 and bi ==1:
        x = d//366
        y = y+x
        d = d%366

    months = bises[0] #months depending from type of year (bis or not)

    count = 0
    m = 1
    day = 0
    while d > 28:
        day = d
        d = d - months[m-1]
        if d>0:
            day = d
            m = m+1
            print('month',m)



    return y, m, day



def main():
    datey1 = int(input('Enter a year for the first date:'))
    dated1 = int(input('Enter a day for the first date (ordinal):'))
    ret_plus = 280

    pur = greg_date(datey1,dated1)
    print('You did the purchase in:', pur)
    ret=greg_date(datey1,dated1,ret_plus)
    print('The retail time is:',ret)

if __name__ == "__main__":
        main()