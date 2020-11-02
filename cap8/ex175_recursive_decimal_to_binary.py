#define a recursive function to convert a non-negative
#integer entered by the user from decimal to binary.
def decimal_to_binary(lis,n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        c=n%2
        q=n//2
        lis=str(c)
        return lis + str(decimal_to_binary(lis,q))
#define the main function
def main():
    #read a non-negative decimal number from the user
    line = int(input("Enter a non-negative decimal number: "))

    if line<0:
        print("That's not a non-negative decimal number!")
    else:
       print(decimal_to_binary('',line)[::-1])

#call the main function
main()

