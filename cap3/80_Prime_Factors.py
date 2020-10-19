#Read an integer number from user
n = int(input("Enter a integer (2 or greater): "))

#Inizializate
factor = 2

#While factor is less than or equal to n do
#If n is evenly divisible by factor then
#Conclude that factor is a factor of n
#Divide n by factor using floor division
#Else
#Increase factor by 1
if n>=2:
    print("The prime factors of",n,"are:")
    while factor<=n:
        if n%factor==0:
            print(factor)
            n=n/factor
        else:
            factor+=1
else:
    print("The entered number is less than 2.")