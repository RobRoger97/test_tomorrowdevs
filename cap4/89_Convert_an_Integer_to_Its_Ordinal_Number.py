def integer(n):
    if n==1:
        name="First"
    elif n==2:
        name="Second"
    elif n==3:
        name="Third"
    elif n==4:
        name="Fourth"
    elif n==5:
        name="Fifth"
    elif n==6:
        name="Sixth"
    elif n==7:
        name="Seventh"
    elif n==8:
        name="Eighth"
    elif n==9:
        name="Ninth"
    elif n==10:
        name="Tenth"
    elif n==11:
        name="Eleventh"
    elif n==12:
        name="Twelfth"
    return name
    if n<1 or n>12:
        return ""

def main():
    for i in range(1,12+1):
        print(integer(i))

if __name__ == "__main__":
    main()
