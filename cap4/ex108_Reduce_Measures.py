

def reduceMeasure(n,u):
    if u == 'teaspoons' or u == 'teaspoon':
        cup = 0
        tab = 0
        teas = n
        if teas >= 3:
            at = teas // 3
            tab+= at
            teas = teas % 3

        if tab >= 16:
            tt = tab // 16
            cup+= tt
            tab = tab % 16
    elif u == 'tablespoons' or u == 'tablespoon':
        cup = 0
        tab = n
        teas = 0
        if tab >= 16:
            tt = tab // 16
            cup+= tt
            tab = tab % 16
    elif u == 'cup' or u == 'cups':
        cup = n
        tab = 0
        teas = 0
    else:
        cup = 0
        tab = 0
        teas = 0

    print(cup,'Cups', tab,'Tablespoons', teas,'Teaspoons')
    return (cup,tab,teas)

def main():
    num = int(input('Number of units:'))
    unit = str(input('Unit of measure:'))

    reduceMeasure(num,unit)

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()