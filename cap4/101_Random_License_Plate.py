
from random import randint

#Define plate function for a random old or new plate
def plate():
    n = randint(0, 1)
    res =''
    x = 1
#Old plate
    if n==0:
        while x<=3:
            a = randint(65, 90)
            al = chr(a)
            res+=al
            x+=1
        while 4<= x<=6:
            b = randint(0, 9)
            b = str(b)
            res+=b
            x+=1
#New plate
    else:
        while x<=4:
            b = randint(0, 9)
            b = str(b)
            res+=b
            x+=1
        while 5<= x<=7:
            a = randint(65, 90)
            al = chr(a)
            res+=al
            x+=1

    return res

#Define main
def main():
#Display the result
    print(plate())
    
# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()