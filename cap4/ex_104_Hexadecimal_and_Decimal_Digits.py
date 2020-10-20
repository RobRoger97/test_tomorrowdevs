#The hex2int function is responsible for converting a string containing a single
#hexadecimal digit to a base 10 integer 
def hex2int(x):
    n = len(x) - 1
    tot = 0
    for a in x:
        if '0' <= a <= '9':
            a = int(a)
            b = a * (16 ** n)
        elif a == 'A':
            a = 10
            b = a * (16 ** n)
        elif a == 'B':
            a = 11
            b = a * (16 ** n)
        elif a == 'C':
            a = 12
            b = a * (16 ** n)
        elif a == 'D':
            a = 13
            b = a * (16 ** n)
        elif a == 'E':
            a = 14
            b = a * (16 ** n)
        elif a == 'F':
            a = 15
            b = a * (16 ** n)
        else:
            print('something went wrong')
            break
        tot+=b
        n-=1

    return tot
#the int2hex function is responsible for converting an integer
#between 0 and 15 to a single hexadecimal digit. 
def int2hex(q):
    res = ''
    while q != 0:
        r = q % 16
        r = str(r)
        if r == '10':
            r = 'A'
        elif r == '11':
            r = 'B'
        elif r == '12':
            r = 'C'
        elif r == '13':
            r = 'D'
        elif r == '14':
            r = 'E'
        elif r == '15':
            r = 'F'
        elif '0'<= r <= '9':
            r = r
        else:
            print('something went wrong')
            break
        res+=r
        q = q // 16

    c = len(res)
    counter = -1
    res_new = ''
    for x in res:
        counter+= 1
        d = c - counter
        e = c - counter - 1
        f = res[e:d]
        res_new+=f
        print(x)


    return res_new

def main():
    string1 = input("Enter a hexadecimal digits: ")
    print("That in decimal digits is:",hex2int(string1))

    string2 = int(input("Enter a decimal digits: "))
    print("That in hexadecimal digits is:",int2hex(string2))

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()