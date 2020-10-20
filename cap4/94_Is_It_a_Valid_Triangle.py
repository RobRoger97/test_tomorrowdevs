#Define triangle function
def triangle(a,b,c):
    if a>= b+c:
        d = False
    elif b>= a+c:
        d = False
    elif c>= b+a:
        d = False
    else:
        d = True

    return d

#define main
def main():
#read first,second and tirth sides
    l1=int(input('Enter the first side of the triangle:'))
    l2=int(input('Enter the second side of the triangle:'))
    l3=int(input('Enter the third side of the triangle:'))

#display the result
    print(triangle(l1,l2,l3))

if __name__ == "__main__":
        main()
